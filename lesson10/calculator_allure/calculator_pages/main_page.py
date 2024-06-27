import allure
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FfDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """Класс предоставляет методы для выполнения UI-тестов на странице калькулятора"""
    
    _driver: ChromeDriver | FfDriver
    _wait: WebDriverWait
    
    def __init__(self, driver:  ChromeDriver | FfDriver) -> None:
        """
            Создание экземпляра класса MainPage
            :param driver(ChromeDriver | FfDriver): веб-драйвер браузера
            
            :return: None
          """
        self._driver = driver
        self._wait = WebDriverWait(driver, 4)
      
    @allure.step('Перейти на страницу сайта')
    def open(self) -> None:
        """
            Открытие страницы калькулятор
            
            :return: None
        """
        
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#calculator')))
    
    @allure.step('Установить время ожидания {delaying} секунд') 
    def set_delay(self, delaying: int) -> None:
        """
            Установить время ождания
            :param delaying(int): время задержки в секундах
            
            :return: None
        """
          
        self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#delay')))
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(delaying)
     
    @allure.step('Нажать кнопку с цифрой {number}') 
    def press_number_button(self, number: int) -> None:
        """
            Нажатие кнопки с цифрой
            :param number(int): цифра на кнопке калькулятора
            
            :return: None
        """
        
        self._driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-primary") and text() = "{number}"]').click()
    
    @allure.step('Нажать кнопку с оператором {operator}') 
    def press_operator_button(self, operator: str) -> None:
        """
            Нажатие кнопки с оператором
            :param operator(str): математическое действие в формате '+', '-', '/', '*'
            
            :return: None
        """
        
        self._driver.find_element(By.XPATH, f'//span[contains(@class, "operator btn btn-outline-success") and text() = "{operator}"]').click()
      
    @allure.step('Нажать кнопку с равно') 
    def press_equal_button(self) -> None:
        """
            Нажатие кнопки равно
            
            :return: None
        """
        
        self._driver.find_element(By.XPATH, f'//span[contains(@class, "btn btn-outline-warning") and text() = "="]').click()

    @allure.step('Ответ на калькуляторе соответствует переданному значению {result} после {delaying} секунд ожидания') 
    def get_result_after_delayed(self, delaying: float, result: str) -> bool:
        """
            Сравнение итогового значения на калькуляторе с переданным результатом после ожидания
            :param delaying(float): время задержки в секундах
            :param result(str): заранее вычисленное значение

            :return: bool: результат сравнения значений
        """
        
        return WebDriverWait(self._driver, delaying + 1, 0.1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), str(result)))
