from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urlAddress = 'http://the-internet.herokuapp.com/login'

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

username_field_locator = '#username'
pass_field_locator = '#password'
login_btn_locator = 'form#login button[type="submit"]'

driver.find_element(By.CSS_SELECTOR, username_field_locator).send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, pass_field_locator).send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, login_btn_locator).click()

if driver.current_url.split('/')[-1] == 'secure':
  print('success login')
else:
  print('error in login') 

sleep(10)

driver.quit()