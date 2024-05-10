from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

urlAddress = 'http://the-internet.herokuapp.com/add_remove_elements/'
count = 5

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(urlAddress)

add_btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
for i in range(0, count):
  add_btn.click()

delete_btns = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')
print(len(delete_btns))

sleep(10)

driver.quit()
