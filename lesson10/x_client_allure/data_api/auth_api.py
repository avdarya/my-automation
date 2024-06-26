import requests 
import allure

class AuthApi:
    """Класс предоставляет методы для отправки на сервер приложения API-запросов на авторизацию"""
    base_url: str
    
    def __init__(self, base_url: str) -> None:
        """
            Создание экземпляра класса AuthApi
            :param base_url(str): базовый url-адрес
            
            :return: None
        """
        self.base_url = base_url
      
    @allure.step('api. Получить токен авторизации для пользователя {username}:{password}')
    def get_token(self, username: str, password: str) -> str:
        """
            Получение токена авторизации
            :param username(str): логин пользователя
            :param password(str): пароль пользователя
            
            :return: str: токен
        """
        body = {
            "username": username,
            "password": password
        }
        resp = requests.post(f'{self.base_url}/auth/login', json=body)
        return resp.json()['userToken']