import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()


url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(10)


lamps = driver.find_elements(By.CLASS_NAME, '_Ud0k')

print(lamps)

parsed_data = []
if not lamps:
       print("Нет найденных светильников")

for lamp in lamps:
   try:

       title = lamp.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
       print(f"Title: {title}")

       price = lamp.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
       print(f"Price: {price}")

       link = lamp.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
       print(f"Link: {link}")

   except:
      print("произошла ошибка при парсинге: {e}")
      continue


   parsed_data.append([title, price, link])

driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
    writer.writerows(parsed_data)