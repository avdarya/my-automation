from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.fullscreen_window()

# driver.get('https://www.google.ru/?hl=ru')
driver.get('https://habr.com/ru/feed/')
# driver.get('https://openweathermap.org/')
# driver.back()
# driver.forward()
# driver.refresh()
# driver.set_window_size(640, 480)
# driver.save_screenshot('./google.png')

sleep(15)