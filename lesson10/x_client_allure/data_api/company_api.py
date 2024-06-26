import requests
import allure
from requests import Response

class CompanyApi:
    """Класс предоставляет методы для отправки на сервер приложения API-запросов по компаниям"""
    base_url: str
  
    def __init__(self, base_url: str) -> None:
        """
            Создание экземпляра класса CompanyApi
            :param base_url(str): базовый url-адрес
            
            :return: None
        """
        
        self.base_url = base_url
   
    @allure.step('api. Создать компанию с названием {name} ({description})')
    def create_company(self,  headers: dict, name: str, description: str = '') -> Response:
        """
            Создание компании
            :param headers(dict): заголовки запроса с данными для авторизации
            :param name(str): название компании
            :param description(str): (optional) описание компании
            
            :return: Response: ответ http-запроса
        """
        
        body = {
          "name": name,
          "description": description
        }
        return requests.post(f'{self.base_url}/company', headers=headers, json=body)
    
    @allure.step('api. Получить список компаний с параметрами запроса ({params})')
    def get_company_list(self, params: dict | None = None) -> Response:
        """
            Получение списка компаний
            :param params(dict | None): (optional) параметры запроса
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/company', params=params)
    
    @allure.step('api. Получить компанию по id - {id}')
    def get_company_by_id(self, id: int) -> Response:
        """
            Получение компании по id
            :param id(int): id компании
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/company/{str(id)}')
    
    @allure.step('api. Отредактировать компанию')
    def edit_company(self, headers: dict, id: int, name: str, descr: str) -> Response:
        """
            Редактирование компании
            :param headers(dict): заголовки запроса с данными для авторизации
            :param id(int): id компании
            :param name(str): название компании
            :param description(str): описание компании
            
            :return: Response: ответ http-запроса
        """
        
        body = {
          'name': name,
          'description': descr
        }
        return requests.patch(f'{self.base_url}/company/{str(id)}', headers=headers, json=body)
    
    @allure.step('api. Удалить компанию')
    def delete_company(self, headers: dict, id: int) -> Response:
        """
            Удаление компании
            :param headers(dict): заголовки запроса с данными для авторизации
            :param id(int): id компании
            
            :return: Response: ответ http-запроса
        """
        
        return requests.get(f'{self.base_url}/company/delete/{str(id)}', headers=headers)
    
    @allure.step('api. (Де)активировать компанию c id {id} -> {is_active}')
    def set_status(self, headers: dict, id: int, is_active: bool) -> Response:
        """
            Изменение статуса компании
            :param headers(dict): заголовки запроса с данными для авторизации
            :param id(int): id компании
            :param is_active(bool): статус активности компании
            
            :return: Response: ответ http-запроса
        """
        
        return requests.patch(f'{self.base_url}/company/status/{str(id)}', headers=headers, json={"isActive": is_active})