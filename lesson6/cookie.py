from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

my_cookie = {
  'name': 'cookie_policy',
  'value': '1'
}

driver.get('https://labirint.ru')
driver.add_cookie(my_cookie)

cookies = driver.get_cookies()
print(cookies)

cookie_by_name = driver.get_cookie('_ga_21PJ900698')
print(cookie_by_name)

# driver.refresh()

# driver.delete_all_cookies()
# driver.delete_cookie('cookie_policy')

# sleep(5)
driver.quit()

