from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urlAddress = 'http://the-internet.herokuapp.com/inputs'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(urlAddress)

field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

field.send_keys('1000')
sleep(1)

field.clear()
sleep(1)

field.send_keys('990')
for i in range(0, 9):
  field.send_keys(Keys.ARROW_UP)

sleep(10)

driver.quit()