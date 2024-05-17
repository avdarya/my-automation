from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def make_screenshot(browser):
  browser.maximize_window()
  browser.get('https://dzen.ru/')
  sleep(5)
  browser.save_screenshot('./lesson6/dzen_'+browser.name+'.png')
  browser.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

options = FFOptions()
options.page_load_strategy = 'normal'
ff = webdriver.Firefox(options=options)

safariOptions = SafariOptions()
safariOptions.page_load_strategy = 'normal'
safari = webdriver.Safari(options=safariOptions)



make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(safari)
