from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/checkboxes')

div = driver.find_element(By.CSS_SELECTOR, '#page-footer')
a = div.find_element(By.CSS_SELECTOR, 'a')
print(a.get_attribute('href'))

divs = driver.find_elements(By.CSS_SELECTOR, 'div')
css_class = divs[6].get_attribute('class')
print(css_class)

divs = driver.find_elements(By.CSS_SELECTOR, 'dfsdf')
print(len(divs))

sleep(2)

driver.quit()