from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urlAddress = 'http://the-internet.herokuapp.com/login'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(urlAddress)

driver.find_element(By.CSS_SELECTOR, '#username').send_keys('tomsmith')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('SuperSecretPassword!')
driver.find_element(By.CSS_SELECTOR, 'form#login button[type="submit"]').click()

if driver.current_url.split('/')[-1] == 'secure':
  print('success login')
else:
  print('error in login') 

sleep(10)

driver.quit()