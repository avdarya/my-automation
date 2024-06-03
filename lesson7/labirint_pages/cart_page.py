from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
  _driver: ChromeDriver | FfDriver
  _wait: WebDriverWait
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    self._wait = WebDriverWait(driver, 4)
    
  def open(self) -> None:
    self._driver.get('https://www.labirint.ru/cart/')
    
  def get_cart_counter(self) -> int:
    cart_count = self._driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"] b').text
    return int(cart_count)