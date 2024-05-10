from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

urlAddress = 'http://uitestingplayground.com/dynamicid'
count = 3

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

btn_locator = 'button.btn-primary'

for i in range(0, count):
  click_btn = driver.find_element(By.CSS_SELECTOR, btn_locator)
  click_btn.click()
  print(click_btn.get_attribute('id'))
  driver.refresh()

sleep(10)

driver.quit()
