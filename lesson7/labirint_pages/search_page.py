from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
  _driver: ChromeDriver | FfDriver
  _wait: WebDriverWait
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    self._wait = WebDriverWait(driver, 7)
    
  def add_to_cart(self) -> int:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section[class="search-tab"]')))
    buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, '._btn.btn-tocart.buy-link')
    counter = 0
    for btn in buy_buttons:
      btn.click()
      counter += 1
      
    return counter
  
  def get_empty_result_msg(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, 'div[class="search-error bestsellers"] h1').text