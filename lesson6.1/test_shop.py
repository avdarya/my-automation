import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('login, password, goods, first_name, last_name, zip_code, total', 
  [
    (
      'standard_user',
      'secret_sauce',
      'Sauce Labs Backpack^Sauce Labs Bolt T-Shirt^Sauce Labs Onesie',
      'Darya',
      'Tsy',
      '159000',
      '$58.29'
    )
  ]
)
def test_purchase(login, password, goods, first_name, last_name, zip_code, total):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
  driver.get('https://www.saucedemo.com/')

  driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys(login)
  driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(password)
  driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()

  good_list = str(goods).split('^')
  loaded_goods = driver.find_elements(By.CSS_SELECTOR, 'div.inventory_item')
  for loaded_good_item in loaded_goods:
    for good_item in good_list:
      if loaded_good_item.find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text == good_item:
        loaded_good_item.find_element(By.CSS_SELECTOR, 'button.btn_inventory').click()
  
  driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
  
  driver.find_element(By.CSS_SELECTOR, '#checkout').click()

  driver.find_element(By.CSS_SELECTOR, '#first-name').clear()
  driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
  driver.find_element(By.CSS_SELECTOR, '#last-name').clear()
  driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
  driver.find_element(By.CSS_SELECTOR, '#postal-code').clear()
  driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(zip_code)
  driver.find_element(By.CSS_SELECTOR, '#continue').click()
  
  assert total in driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text

  driver.quit()