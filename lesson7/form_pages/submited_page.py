from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

class SubmitedPage:
  _driver: ChromeDriver | FfDriver
  
  def __init__(self, driver: ChromeDriver | FfDriver) -> None:
    self._driver = driver
    WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div[class="row"]')))
   
  def get_first_name_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
  
  def get_first_name_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('border-color')
  
  def get_last_name_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
  
  def get_last_name_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('border-color')
  
  def get_address_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
  
  def get_address_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('border-color')
  
  def get_email_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
  
  def get_email_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('border-color')
  
  def get_phone_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
  
  def get_phone_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('border-color')
  
  def get_city_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
  
  def get_city_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('border-color')
  
  def get_country_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
  
  def get_country_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('border-color')
  
  def get_job_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
  
  def get_job_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('border-color')
  
  def get_company_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
  
  def get_company_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('border-color')
  
  def get_zip_code_bg_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
  
  def get_zip_code_brd_color(self) -> str:
    return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('border-color')
