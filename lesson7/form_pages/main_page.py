from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
  _driver: ChromeDriver | FfDriver
  
  def __init__(self, driver: ChromeDriver | FfDriver) -> None:
    self._driver = driver
    
  def open(self):
    self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    WebDriverWait(self._driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR,'form[action="data-types-submitted.html"]')))

  def set_first_name(self, first_name: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
    
  def set_last_name(self, last_name: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
  
  def set_address(self, address: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
      
  def set_email(self, email: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
      
  def set_phone(self, phone: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
  
  def set_city(self, city: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
    
  def set_country(self, country: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
  
  def set_job(self, job: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job)
        
  def set_company(self, company: str) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').clear()
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
    
  def clear_zip_code(self) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    
  def submit(self) -> None:
    self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
