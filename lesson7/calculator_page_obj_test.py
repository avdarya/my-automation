import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_pages.main_page import MainPage

@pytest.mark.parametrize('delaying, num_1, operator, num_2, result', [(45, 7, '+', 8, 15)])
def test_calc_two_nums(delaying: int, num_1: int, operator: str, num_2: int, result: int):
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  
  main_page = MainPage(driver)
  main_page.open()
  
  main_page.set_delay(delaying)
  
  main_page.press_number_button(num_1)
  main_page.press_operator_button(operator)
  main_page.press_number_button(num_2)
  main_page.press_equal_button()
 
  assert main_page.get_result_after_delayed(float(delaying), str(result))

  driver.quit()