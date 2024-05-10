from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

urlAddress = 'http://the-internet.herokuapp.com/inputs'

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

field_locator = 'input[type="number"]'

field = driver.find_element(By.CSS_SELECTOR, field_locator)

field.send_keys('1000')
sleep(1)

field.clear()
sleep(1)

field.send_keys('990')
for i in range(0, 9):
  field.send_keys(Keys.ARROW_UP)

sleep(10)

driver.quit()