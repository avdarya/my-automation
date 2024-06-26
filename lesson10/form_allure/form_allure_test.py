import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from form_pages.main_page import MainPage
from form_pages.submited_page import SubmitedPage
from time import sleep

@allure.epic('Заполнение формы')
@allure.severity(allure.severity_level.MINOR)
@allure.suite('UI-тесты по заполнению формы на сайте и валидации пустых полей')
class FormTest:
  
    @allure.id('f_1')
    @allure.story('Подкрашивание пустых и заполненных полей при отправке формы')
    @allure.title('Пустое поле индекс подсвечено красным + заполненные поля подсвечены зеленым')
    @allure.description('Заполнить все поля формы, кроме поля индекс, корректными значениями')
    @allure.feature('CHECK CSS: background-color + border-color')
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
              '#f5c2c7'
          )
      ]
    )
    def test_empty_zip_code(
        self,
        first_name: str, 
        last_name: str, 
        address: str, 
        email: str, 
        phone: str, 
        city: str, 
        country: str, 
        job: str, 
        company: str,   
        success_bg_color: str, 
        success_brd_color: str, 
        error_bg_color: str, 
        error_brd_color: str
    ):
        with allure.step('Создать экземпляр веб-драйвера браузера Chrome'):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        main_page = MainPage(driver)
        main_page.open()

        main_page.set_first_name(first_name)
        main_page.set_last_name(last_name)
        main_page.set_address(address)
        main_page.set_email(email)
        main_page.set_phone(phone)
        main_page.set_city(city)
        main_page.set_country(country)
        main_page.set_job(job)
        main_page.set_company(company)
        
        main_page.clear_zip_code()
        
        main_page.submit()

        submited_page = SubmitedPage(driver)

        errors = []
          
        with allure.step('Проверить, что у пустого поля индекс CSS-свойства background-color и border-color соответствуют danger'):
            if not self.is_colors_match(submited_page.get_zip_code_bg_color(), error_bg_color):
                errors.append('ERROR in danger background-color css property for zip-code field')
            if not self.is_colors_match(submited_page.get_zip_code_brd_color(), error_brd_color):
                errors.append('ERROR in danger border-color css property for zip-code field')
            
        with allure.step('Проверить, что у заполненного поля имя CSS-свойства background-color и border-color соответствуют success'):    
            if not self.is_colors_match(submited_page.get_first_name_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for first-name field')
            if not self.is_colors_match(submited_page.get_first_name_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for first-name field')
        
        with allure.step('Проверить, что у заполненного поля фамилия CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_last_name_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for last-name field')
            if not self.is_colors_match(submited_page.get_last_name_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for last-name field')
        
        with allure.step('Проверить, что у заполненного поля адрес CSS-свойства background-color и border-color соответствуют success'):     
            if not self.is_colors_match(submited_page.get_address_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for address field')
            if not self.is_colors_match(submited_page.get_address_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for address field')
        
        with allure.step('Проверить, что у заполненного поля email CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_email_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for email field')
            if not self.is_colors_match(submited_page.get_email_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for email field')
        
        with allure.step('Проверить, что у заполненного поля телефон CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_phone_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for phone field')
            if not self.is_colors_match(submited_page.get_phone_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for phone field')
        
        with allure.step('Проверить, что у заполненного поля город CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_city_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for city field')
            if not self.is_colors_match(submited_page.get_city_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for city field')
        
        with allure.step('Проверить, что у заполненного поля страна CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_country_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for country field')
            if not self.is_colors_match(submited_page.get_country_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for country field')
        
        with allure.step('Проверить, что у заполненного поля работа CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_job_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for job field')
            if not self.is_colors_match(submited_page.get_job_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for job field')
        
        with allure.step('Проверить, что у заполненного поля компания CSS-свойства background-color и border-color соответствуют success'):       
            if not self.is_colors_match(submited_page.get_company_bg_color(), success_bg_color):
                errors.append('ERROR in success background-color css property for company field')
            if not self.is_colors_match(submited_page.get_company_brd_color(), success_brd_color):
                errors.append('ERROR in success border-color css property for company field')
        
        with allure.step('Проверка: ошибок в CSS-свойствах background-color и border-color у полей отправленной формы не найдено'): 
            assert not errors, "errors occured:\n{}".format("\n".join(errors))

        driver.quit()

    def is_colors_match(self, as_is: str, to_be: str) -> bool:
        return Color.from_string(as_is).hex == to_be
