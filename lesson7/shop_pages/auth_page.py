from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
  _driver: ChromeDriver | FfDriver
  
  def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
    self._driver = driver
    
  def open(self) -> None:
    self._driver.get('https://www.saucedemo.com/')
    WebDriverWait(self._driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="login-box"]')))
    
  def set_user_name(self, user_name: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input#user-name').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input#user-name').send_keys(user_name)
  
  def set_password(self, password: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input#password').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(password)
    
  def login(self) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input#login-button').click()
