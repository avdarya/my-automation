from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://dzen.ru')

driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
sleep(2)
driver.set_window_size(500, 640)
sleep(2)

driver.quit()