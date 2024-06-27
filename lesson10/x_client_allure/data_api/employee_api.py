import allure
import requests
from requests import Response

class EmployeeApi:
    """Класс предоставляет методы для отправки на сервер приложения API-запросов по сотрудникам"""
    base_url: str
    
    def __init__(self, base_url: str) -> None:
        """
            Создание экземпляра класса EmployeeApi
            :param base_url(str): базовый url-адрес
            
            :return: None
        """
        self.base_url = base_url
    
    @allure.step('api. Получить сотрудников в компании с id {company_id}')
    def get_by_company(self, company_id: int) -> Response:
        """
            Получение списка сотрудников компании
            :param company_id(int): id компании
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/employee', params={'company': company_id})
    
    @allure.step('api. Получить сотрудников без указания компании (негативная проверка)')
    def get_without_company(self) -> Response:
        """
            Негативная проверка на получение списка сотрудников без указания компании
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/employee')
    
    @allure.step('api. Создать сотрудника с данными {body}')
    def create(self, headers: dict, body: dict) -> Response:
        """
            Создание сотрудника
            :param headers(dict): заголовки запроса с данными для авторизации
            :param body(dict): тело запроса
            
            :return: Response: ответ http-запроса
        """
        
        return requests.post(f'{self.base_url}/employee', headers=headers, json=body)
    
    @allure.step('api. Создать сотрудника без передачи данных (негативная проверка)')
    def create_without_body(self, headers: dict) -> Response:
        """
            Негативная проверка на созадние сотрудников без передачи тела запроса
            :param headers(dict): заголовки запроса с данными для авторизации
            
            :return: Response: ответ http-запроса
        """
        
        return requests.post(f'{self.base_url}/employee', headers=headers)
    
    @allure.step('api. Получить сотрудника по id {employee_id}')
    def get_by_id(self, employee_id: int) -> Response:
        """
            Получение сотрудника по id
            :param employee_id(int): id сотрудника
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/employee/{employee_id}')
    
    @allure.step('api. Получить сотрудника без передачи id (негативная проверка)')
    def get_without_id(self) -> Response:
        """
            Негативная проверка на получение сотрудников без передачи id
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/employee')
    
    @allure.step('api. Отредактировать сотрудника с id {id} обновленными данными {body}')
    def edit(self, headers: dict, id: int, body: dict) -> Response:
        """
            Редактирование сотрудника
            :param headers(dict): заголовки запроса с данными для авторизации
            :param id(int): id сотрудника
            :param body(dict): тело запроса
            
            :return: Response: ответ http-запроса
        """
        
        return requests.patch(f'{self.base_url}/employee/{id}', headers=headers, json=body)
    
    @allure.step('api. Отредактировать сотрудника без передачи id (негативная проверка)')
    def edit_without_id(self, headers: dict, body: dict) -> Response:
        """
            Негативная проверка на редактирование сотрудника без передачи id
            :param headers(dict): заголовки запроса с данными для авторизации
            :param body(dict): тело запроса
            
            :return: Response: ответ http-запроса
        """
        
        return requests.patch(f'{self.base_url}/employee', headers=headers, json=body)
    
    @allure.step('api. Отредактировать сотрудника с id {id} без передачи данных (негативная проверка)')
    def edit_without_body(self, headers: dict, id: int) -> Response:
        """
            Негативная проверка на редактирование сотрудника без передачи тела запроса
            :param headers(dict): заголовки запроса с данными для авторизации
            :param id(int): id сотрудника
            
            :return: Response: ответ http-запроса
        """
        
        return requests.patch(f'{self.base_url}/employee/{id}', headers=headers)