from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urlAddress = 'http://the-internet.herokuapp.com/entry_ad'

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Firefox(options=options)

driver.get(urlAddress)

close_btn_locator = 'div.modal-footer p'
modal_locator = '#modal'

wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of(driver.find_element(By.CSS_SELECTOR, modal_locator)))

sleep(1)
close_btn = driver.find_element(By.CSS_SELECTOR, close_btn_locator)
close_btn.click()

sleep(10)

driver.quit()