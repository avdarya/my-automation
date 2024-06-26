from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutOneStep:
  _driver: ChromeDriver | FfDriver
  _wait: WebDriverWait
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    self._wait = WebDriverWait(driver, 4)
    
  def set_first_name(self, first_name: str) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="checkout_info"]')))
    self._driver.find_element(By.CSS_SELECTOR, '#first-name').clear()
    self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)

  def set_last_name(self, last_name: str) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="checkout_info"]')))
    self._driver.find_element(By.CSS_SELECTOR, '#last-name').clear()
    self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
  
  def set_postal_code(self, postal_code: str) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="checkout_info"]')))
    self._driver.find_element(By.CSS_SELECTOR, '#postal-code').clear()
    self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
  
  def press_continue(self) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="checkout_buttons"]')))
    self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
