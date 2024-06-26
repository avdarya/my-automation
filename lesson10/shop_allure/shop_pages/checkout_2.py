from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutTwoStep:
  _driver: ChromeDriver | FfDriver
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    
  def get_summary_total(self) -> str:
    WebDriverWait(self._driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="summary_info"]')))
    return self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text