from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

cookies = { 'name': 'cookie_policy', 'value': '1' }
  
def test_cart_counter():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  wait = WebDriverWait(driver, 7)
  
  # перейти на сайт
  driver.get('https://www.labirint.ru/')

  driver.add_cookie(cookies)
  
  # найти книги по слову python
 
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[id="search-field"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[id="search-field"]').clear()
  driver.find_element(By.CSS_SELECTOR, 'input[id="search-field"]').send_keys('python')
  driver.find_element(By.CSS_SELECTOR, 'button[type="submit"][form="searchform"]').click()
    
  # добавить все книги в корзину и посчитать
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section[class="search-tab"]')))
  buy_buttons = driver.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
  counter = 0
  for btn in buy_buttons:
    btn.click()
    counter += 1
  
  # перейти в корзину
  driver.get('https://www.labirint.ru/cart/')
  
  # проверить счетчик товаров в корзине == кол-ву нажатий
  cart_count = driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"] b').text
  
  assert counter == int(cart_count)
   
  driver.quit()