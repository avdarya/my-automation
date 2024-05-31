from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from labirint_pages.main_page import MainPage
from labirint_pages.search_page import SearchPage
from labirint_pages.cart_page import CartPage
  
def test_cart_counter():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  
  # перейти на сайт
  main_page = MainPage(driver)
  main_page.open()
  main_page.set_cookie_policy()
  
  # найти книги по слову python с переходом на search page
  main_page.search('python')
 
  # добавить все книги в корзину и посчитать
  search_page = SearchPage(driver)
  added_count = search_page.add_to_cart()

  # перейти в корзину
  cart_page = CartPage(driver)
  cart_page.open()
  
  # получить значение счетчика в корзине
  cart_count = cart_page.get_cart_counter()
  
  # проверить счетчик товаров в корзине == кол-ву нажатий  
  assert added_count == cart_count
  
  driver.quit()
  
def test_empty_serch_result():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  
  main_page = MainPage(driver)
  main_page.open()
  main_page.search('no book search term')
  
  search_page = SearchPage(driver)
  as_is = search_page.get_empty_result_msg()

  assert 'Мы ничего не нашли по вашему запросу! Что делать?' == as_is
  
  driver.quit()