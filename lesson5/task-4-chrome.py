from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urlAddress = 'http://the-internet.herokuapp.com/entry_ad'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(urlAddress)

wait = WebDriverWait(driver, 2)
wait.until(EC.visibility_of(driver.find_element(By.CSS_SELECTOR, '#modal')))

sleep(1)
close_btn = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer p')
close_btn.click()

sleep(10)

driver.quit()
