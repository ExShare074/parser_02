import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divanparscraper"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/divany-i-kresla"]

    def __init__(self, *args, **kwargs):
        super(DivannewparsSpider, self).__init__(*args, **kwargs)
        self.crawled_data = []  # Инициализация списка для накопления данных

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            relative_url = divan.css('a').attrib.get('href', '')
            url = response.urljoin(relative_url)

            # Сохранение данных в атрибут crawled_data
            self.crawled_data.append({
                'name': name,
                'price': price,
                'url': url
            })

            # Передача данных для pipeline или других обработчиков
            yield {
                'name': name,
                'price': price,
                'url': url
            }

    def close(self, reason):
        # Запись данных в CSV-файл при завершении парсинга
        try:
            with open("divanscraper.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Название дивана", "Цена", "Ссылка на диван"])
                for item in self.crawled_data:
                    writer.writerow([item['name'], item['price'], item['url']])
        except Exception as e:
            self.logger.error(f"Произошла ошибка при записи в файл: {e}")
