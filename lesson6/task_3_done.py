from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

wait = WebDriverWait(driver, 40)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done!'))

images = driver.find_elements(By.CSS_SELECTOR, '#image-container img')

src_3 = images[2].get_attribute('src')
print(src_3)

driver.quit()