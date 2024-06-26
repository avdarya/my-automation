import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from shop_pages.auth_page import AuthPage
from shop_pages.inventory_page import InventoryPage
from shop_pages.cart_page import CartPage
from shop_pages.checkout_1 import CheckOutOneStep
from shop_pages.checkout_2 import CheckOutTwoStep

@allure.epic('Оформление заказа в интернет-магазине')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('UI-тесты по оформлению заказа в интернет-магазине')
class ShopTest:
    @allure.id('p_1')
    @allure.story('Оформления заказа (позитив)')
    @allure.title('Правильность отображения итоговой суммы заказа')
    @allure.description('Добавить товары в корзину и проверить отображение итоговой суммы заказа на странице информация о заказе')
    @allure.feature('purchase')
    @pytest.mark.parametrize('user_name, password, goods, first_name, last_name, postal_code, total', 
        [
            (
                'standard_user',
                'secret_sauce',
                'Sauce Labs Backpack^Sauce Labs Bolt T-Shirt^Sauce Labs Onesie',
                'Darya',
                'Tsy',
                '159000',
                '$58.29'
            )
        ]
    )
    def test_purchase(
        self,
        user_name: str, 
        password: str, 
        goods: str, 
        first_name: str, 
        last_name: str, 
        postal_code: str, 
        total: str
    ):
        with allure.step('Создать экземпляр веб-драйвера браузера Chrome'):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
        auth_page = AuthPage(driver)
        auth_page.open()
        auth_page.set_user_name(user_name)
        auth_page.set_password(password)
        auth_page.login()

        inventory_page = InventoryPage(driver)
        inventory_list = str(goods).split('^')
        for list_item in inventory_list:
            inventory_page.add_to_cart_by_inventory(list_item)
          
        inventory_page.press_cart()
        
        cart_page = CartPage(driver)
        cart_page.press_checkout()

        checkout_one_page = CheckOutOneStep(driver)
        checkout_one_page.set_first_name(first_name)
        checkout_one_page.set_last_name(last_name)
        checkout_one_page.set_postal_code(postal_code)
        checkout_one_page.press_continue()
        
        checkout_two_page = CheckOutTwoStep(driver)
      
        with allure.step('Проверка: итоговая сумма заказа на странице информации о заказе отображается верно'): 
            assert total in checkout_two_page.get_summary_total()

        driver.quit()