from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://labirint.ru')

txt = driver.find_element(By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount').text
id = driver.find_element(By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount').id
tag = driver.find_element(By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount').tag_name
href = driver.find_element(By.CSS_SELECTOR, 'a.b-header-b-logo-e-discount').get_attribute('href')

color = driver.find_element(By.CSS_SELECTOR, 'span.b-header-b-logo-e-discount-e-amount').value_of_css_property('color')
font_size = driver.find_element(By.CSS_SELECTOR, 'span.b-header-b-logo-e-discount-e-amount').value_of_css_property('font-size')

print(txt)
print(id)
print(tag)
print(href)
print(color)
print(font_size)

sleep(12)

driver.quit()