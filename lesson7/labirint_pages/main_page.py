from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
  _driver: ChromeDriver | FfDriver
  _wait: WebDriverWait
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    self._wait = WebDriverWait(driver, 7)

  def open(self) -> None:
    self._driver.get('https://www.labirint.ru/')
    
  def set_cookie_policy(self) -> None:
    cookies = { 'name': 'cookie_policy', 'value': '1' }
    self._driver.add_cookie(cookies)
    
  def search(self, term: str) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[id="search-field"]')))
    self._driver.find_element(By.CSS_SELECTOR, 'input[id="search-field"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[id="search-field"]').send_keys(term)
    self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"][form="searchform"]').click()
