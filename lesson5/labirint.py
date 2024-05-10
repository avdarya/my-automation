from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.labirint.ru/')

search_locator = 'search-field'
book_locator = 'div.product-card'
author_locator = 'div.product-card__author'
title_locator = 'a.product-card__name'
price_locator = 'div.product-card__price-current'

search_field = driver.find_element(By.ID, search_locator)

search_field.send_keys('Python')
search_field.send_keys(Keys.RETURN)

books = driver.find_elements(By.CSS_SELECTOR, book_locator)

for book in books:
  author = ''
  try:
    author = book.find_element(By.CSS_SELECTOR, author_locator).text
  except:
    author = 'Автор не указан'

  title = book.find_element(By.CSS_SELECTOR, title_locator).text

  price = book.find_element(By.CSS_SELECTOR, price_locator).text

  print(f'{author} "{title}" - {price}')

print('Кол-во книг ' + str(len(books)))

# header_menu_btn_book = 'a[href="/books/"].b-header-b-menu-e-text'
# driver.find_element(By.CSS_SELECTOR, header_menu_btn_book).click()


sleep(10)