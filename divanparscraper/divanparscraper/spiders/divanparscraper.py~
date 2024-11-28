#нужно спарсить с сайта www.divan.ru название диванов, цену, ссылку  и записать в csv
import scrapy
import csv

class DivanparscraperSpider(scrapy.Spider):
    name = "divanparscraper"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div.WdR1o')
        for divan in divans:
            name = divan.css('div.lsooF span::text').get()
            price = divan.css('div.pY3d2 span::text').get()
            url = divan.css('a').attrib['href']
            yield {
                'name': name,
                'price': price,
                'url': url
            }

    def close(self, reason):
        with open("divanscraper.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Название дивана", "Цена", "Ссылка на диван"])
            for item in self.crawled_data:
                writer.writerow([item['name'], item['price'], item['url']])