import allure
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

class SubmitedPage:
    """Класс предоставляет методы для выполнения UI-тестов на странице с отправленной формой"""
    
    _driver: ChromeDriver | FfDriver
    
    def __init__(self, driver: ChromeDriver | FfDriver) -> None:
        """
            Создание экземпляра класса SubmitedPage
            :param driver(ChromeDriver | FfDriver): веб-драйвер браузера
            
            :return: None
        """
        
        self._driver = driver
        WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div[class="row"]')))
      
    def get_first_name_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля имя
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
    
    def get_first_name_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля имя
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('border-color')
    
    def get_last_name_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля фамилия
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
    
    def get_last_name_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля фамилия
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('border-color')
    
    def get_address_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля адрес
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
    
    def get_address_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля адрес
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('border-color')
    
    def get_email_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля email
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
    
    def get_email_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля email
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('border-color')
    
    def get_phone_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля телефон
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
    
    def get_phone_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля телефон
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('border-color')
    
    def get_city_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля город
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
    
    def get_city_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля город
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('border-color')
    
    def get_country_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля страна
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
    
    def get_country_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля страна
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('border-color')
    
    def get_job_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля работа
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
    
    def get_job_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля работа
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('border-color')
    
    def get_company_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля компания
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
    
    def get_company_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля компания
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('border-color')
    
    def get_zip_code_bg_color(self) -> str:
        """
            Получение CSS-свойства background-color у поля индекс
            
            :return: str: значение CSS-свойства background-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    
    def get_zip_code_brd_color(self) -> str:
        """
            Получение CSS-свойства border-color у поля индекс
            
            :return: str: значение CSS-свойства border-color
        """
        
        return self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('border-color')
