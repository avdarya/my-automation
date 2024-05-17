from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# is_displayed
driver.get('http://uitestingplayground.com/visibility')

is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed() # видимость элемента на странице
print(is_displayed)
sleep(2)

driver.find_element(By.CSS_SELECTOR, '#hideButton').click()
sleep(2)

is_displayed = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
print(is_displayed)
sleep(2)

# is_enabled
driver.get('https://demoqa.com/radio-button')

is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(is_enabled)

is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(is_enabled)

# is_selected
driver.get('https://the-internet.herokuapp.com/checkboxes')

cb = driver.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
is_selected = cb.is_selected()
print(is_selected)
sleep(2)

cb.click()
is_selected = cb.is_selected()
print(is_selected)
sleep(2)

driver.quit()