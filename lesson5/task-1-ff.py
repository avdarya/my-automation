from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

urlAddress = 'http://the-internet.herokuapp.com/add_remove_elements/'
count = 5

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

add_btn_locator = 'button[onclick="addElement()"]'
delete_btn_locator = 'button.added-manually'

add_btn = driver.find_element(By.CSS_SELECTOR, add_btn_locator)
for i in range(0, count):
  add_btn.click()

delete_btns = driver.find_elements(By.CSS_SELECTOR, delete_btn_locator)
print(len(delete_btns))

sleep(10)

driver.quit()