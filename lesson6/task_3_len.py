from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

def check_len(browser: WebDriver) -> bool:
  imgs = browser.find_elements(By.CSS_SELECTOR, '#image-container img')
  if len(imgs) == 4:
    return True
  else:
    return False
  
wait = WebDriverWait(driver, 40, 1)
wait.until(check_len)

images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')
src_3 = images[2].get_attribute('src')
print(src_3)

driver.quit()