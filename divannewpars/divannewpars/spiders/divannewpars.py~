#нужно спарсить с сайта www.divan.ru название диванов, цену, ссылку  и записать в csv
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

driver.get(url)
time.sleep(10)  # Уменьшил время ожидания (можно настроить динамическое ожидание)

divans = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')

parsed_data = []

# Парсинг данных
for divan in divans:
    try:
        # Получение данных о диване
        title_element = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.ui-TupxX.ui-IZb9T.e11uu')
        title = title_element.get_attribute('title')
        link = title_element.get_attribute('href')
        price = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text

        # Сохранение в список
        parsed_data.append([title, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
driver.quit()

with open("divan.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название дивана", "Цена", "Ссылка на диван"])
    writer.writerows(parsed_data)