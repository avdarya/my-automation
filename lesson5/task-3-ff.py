from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urlAddress = 'http://uitestingplayground.com/classattr'
count = 3

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

blue_btn_locator = '.btn-primary'

try:
  for i in range(0, count):
    blue_btn = driver.find_element(By.CSS_SELECTOR, blue_btn_locator)
    blue_btn.click()
    
    wait = WebDriverWait(driver, 1)
    wait.until(EC.alert_is_present())

    sleep(1)
    driver.switch_to.alert.dismiss()
    driver.refresh()
except Exception as err:
  print(f"Unexpected {err=}, {type(err)=}")

sleep(10)

driver.quit()