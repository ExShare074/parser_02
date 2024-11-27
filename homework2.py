#нужно спарсить с сайта www.divan.ru название диванов, цену, ссылку  и записать в csv
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/krasnodar/category/divany-i-kresla"

driver.get(url)
time.sleep(30)

divans = driver.find_elements(By.CLASS_NAME, 'div.WdR1o')

parsed_data = []

for divan in divans:
    try:
        title_element = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.ui-TupxX.ui-IZb9T.e11uu').get_attribute('title')
        link = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
        price = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2').text
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

    parsed_data.append([title_element.text, price.text, link])

driver.quit()

with open("divan.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название дивана", "Цена", "Ссылка на диван"])
    writer.writerows(parsed_data)