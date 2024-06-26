import allure
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """Класс предоставляет методы для выполнения UI-тестов на странице по заполнению формы"""
    
    _driver: ChromeDriver | FfDriver
    
    def __init__(self, driver: ChromeDriver | FfDriver) -> None:
        """
            Создание экземпляра класса MainPage
            :param driver(ChromeDriver | FfDriver): веб-драйвер браузера
            
            :return: None
        """
        
        self._driver = driver
    
    @allure.step('Перейти на главную страницу сайта')  
    def open(self):
        """
            Открытие главной страницы с формой
            
            :return: None
        """
        
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        WebDriverWait(self._driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR,'form[action="data-types-submitted.html"]')))

    @allure.step('Ввести в поле имя - {first_name}')
    def set_first_name(self, first_name: str) -> None:
        """
            Заполнить поле имя
            :param first_name(str): имя
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
     
    @allure.step('Ввести в поле фамилия - {last_name}') 
    def set_last_name(self, last_name: str) -> None:
        """
            Заполнить поле фамилия
            :param last_name(str): фамилия
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
    
    @allure.step('Ввести в поле адрес - {address}') 
    def set_address(self, address: str) -> None:
        """
            Заполнить поле адрес
            :param address(str): адрес
            
            :return: None
        """
      
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
    
    @allure.step('Ввести в поле email - {email}')     
    def set_email(self, email: str) -> None:
        """
            Заполнить поле email
            :param email(str): email
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
    
    @allure.step('Ввести в поле телефон - {phone}')     
    def set_phone(self, phone: str) -> None:
        """
            Заполнить поле телефон
            :param phone(str): телефон
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
    
    @allure.step('Ввести в поле город - {city}') 
    def set_city(self, city: str) -> None:
        """
            Заполнить поле город
            :param city(str): город
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
    
    @allure.step('Ввести в поле страна - {country}')  
    def set_country(self, country: str) -> None:
        """
            Заполнить поле страна
            :param country(str): страна
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
    
    @allure.step('Ввести в поле работа - {job}') 
    def set_job(self, job: str) -> None:
        """
            Заполнить поле работа
            :param job(str): работа
            
            :return: None
        """
      
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job)
    
    @allure.step('Ввести в поле компания - {company}')       
    def set_company(self, company: str) -> None:
        """
            Заполнить поле компания
            :param company(str): компания
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').clear()
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
    
    @allure.step('Очистить поле индекс')   
    def clear_zip_code(self) -> None:
        """
            Очистить поле индекс
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').clear()
    
    @allure.step('Нажать кнопку Отправить форму')     
    def submit(self) -> None:
        """
            Нажать кнопку отправить форму
            
            :return: None
        """
        
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
