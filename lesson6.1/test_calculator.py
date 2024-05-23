import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('calc_delay, num_1, operator, num_2, result', [(45, 7, '+', 8, 15)])
def test_calc_two_nums(calc_delay, num_1, operator, num_2, result):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  
  driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

  driver.find_element(By.CSS_SELECTOR, '#delay').clear()
  driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(calc_delay)
  
  driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-primary") and text() = "{num_1}"]').click()
  driver.find_element(By.XPATH, f'//span[contains(@class, "operator btn btn-outline-success") and text() = "{operator}"]').click()
  driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-primary") and text() = "{num_2}"]').click()
  driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-warning") and text() = "="]').click()
   
  wait = WebDriverWait(driver, calc_delay, 0.01)
  assert wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), str(result)))

  driver.quit()