import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from time import sleep

@pytest.mark.parametrize(
  'first_name, ' + 
  'last_name, ' +
  'address, ' +
  'email, ' +
  'phone, ' +
  'city, ' +
  'country, ' +
  'job, ' +
  'company, ' + 
  'success_bg_color, ' +
  'success_brd_color, ' +
  'error_bg_color, ' +
  'error_brd_color',
  [
    (
      'Иван', 
      'Петров', 
      'Ленина, 55-3', 
      'test@skypro.com', 
      '+7985899998787', 
      'Москва', 
      'Россия', 
      'QA', 
      'SkyPro',
      '#d1e7dd', 
      '#badbcc', 
      '#f8d7da', 
      '#f5c2c7',
    )
  ]
)
def test_empty_zip_code(
  first_name, 
  last_name, 
  address, 
  email, 
  phone, 
  city, 
  country, 
  job, 
  company,   
  success_bg_color, 
  success_brd_color, 
  error_bg_color, 
  error_brd_color
):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

  driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
  driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
  driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
  driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
  driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
  driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
  driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
  driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job)
  driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

  driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
  
  driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
  
  errors = []
  
  # test empty zip-code field
  css_bg_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
  if not Color.from_string(css_bg_color).hex == error_bg_color:
    errors.append('test CSS style: alert-danger.background-color. Element with locator -> #zip-code')
  
  css_brd_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('border-color')
  if not Color.from_string(css_brd_color).hex == error_brd_color:
    errors.append('test CSS style: alert-danger.border-color. Element with locator -> #zip-code')
  
  # test correct filled fields
  locators = [
    '#first-name', 
    '#last-name', 
    '#address', 
    '#e-mail', 
    '#phone', 
    '#city', 
    '#country', 
    '#job-position', 
    '#company'
    ]
  for loc in locators:
    css_bg_color = driver.find_element(By.CSS_SELECTOR, loc).value_of_css_property('background-color')
    if not Color.from_string(css_bg_color).hex == success_bg_color:
      errors.append('test CSS style: alert-success.background-color. Element with locator -> ' + loc)
      
    css_brd_color = driver.find_element(By.CSS_SELECTOR, loc).value_of_css_property('border-color')
    if not Color.from_string(css_brd_color).hex == success_brd_color:
      errors.append('test CSS style: alert-success.border-color. Element with locator -> ' + loc)
      
  assert not errors, "errors occured:\n{}".format("\n".join(errors))

  driver.quit()


