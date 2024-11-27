# нужно спарсить с сайта www.divan.ru название диванов, цену, ссылку  и записать в csv
import scrapy
import csv
class DivanparscraperSpider(scrapy.Spider):
    name = "divanparscraper"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/divany-i-kresla"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.crawled_data = []

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            url = response.urljoin(divan.css('a').attrib['href'])
            item = {
                'name': name,
                'price': price,
                'url': url
            }
            self.crawled_data.append(item)
            yield item

    def close(self, reason):
        try:
            with open("divanscraper.csv", "w", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Название дивана", "Цена", "Ссылка на диван"])
                for item in self.crawled_data:
                    writer.writerow([item['name'], item['price'], item['url']])
        except Exception as e:
            print(f"Произошла ошибка при записи в файл: {e}")