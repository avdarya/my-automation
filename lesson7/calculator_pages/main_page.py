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
    self._wait = WebDriverWait(driver, 4)
    
  def open(self) -> None:
    self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#calculator')))
    
  def set_delay(self, delaying: int) -> None:
    self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#delay')))
    self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(delaying)
    
  def press_number_button(self, number: int) -> None:
    self._driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-primary") and text() = "{number}"]').click()
  
  def press_operator_button(self, operator: str) -> None:
    self._driver.find_element(By.XPATH, f'//span[contains(@class, "operator btn btn-outline-success") and text() = "{operator}"]').click()
    
  def press_equal_button(self) -> None:
    self._driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-warning") and text() = "="]').click()

  def get_result_after_delayed(self, delaying: float, result: str) -> bool:
    return WebDriverWait(self._driver, delaying + 1, 0.1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), str(result)))
