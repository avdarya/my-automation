import allure
import pytest
from data_api.auth_api import AuthApi
from data_api.employee_api import EmployeeApi
from data_db.company_table import CompanyTable
from data_db.employee_table import EmployeeTable
from get_auth_header import get_auth_header

@allure.epic('x-client Сотрудники')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('Тесты на API-запросы сотрудников')
class EmployeeTest:
    base_url = 'https://x-clients-be.onrender.com'
    username = 'bloom'
    password = 'fire-fairy'
    database_connection_str = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

    auth_api = AuthApi(base_url)
    empoyee_api = EmployeeApi(base_url)
    company_db = CompanyTable(database_connection_str)
    employee_db = EmployeeTable(database_connection_str)

    @allure.id('empl_1')
    @allure.story('Получение сотрудников компании')
    @allure.title('Получить список сотрудников')
    @allure.description('Получение списка сотрудников по указанной компании')
    @allure.feature('READ')
    @pytest.mark.parametrize('company_name, first_name, last_name, phone', [('Sky Pro', 'Petr', 'Ivanov', '8 999 999 99 99')])
    def test_get_employees_by_company(self, company_name: str, first_name: str, last_name: str, phone: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        employee_body = {
            'first_name': first_name,
            'last_name': last_name,
            'company_id': company_id,
            'phone': phone
        }
        self.employee_db.create_with_required(employee_body)
        employee_id = self.employee_db.get_max_id()

        api_result = self.empoyee_api.get_by_company(company_id)
        
        db_result = self.employee_db.get_employees_by_company(company_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 200
        assert len(api_result.json()) == len(db_result)

    @allure.id('empl_2')
    @allure.story('Получение сотрудников (негатив)')
    @allure.title('Проверка ответа на запрос сотрудников без указания компании')
    @allure.description('Выполнение запроса на получение списка сотрудников без передачи id компании (негативная проверка)')
    @allure.feature('READ')
    def test_get_employees_without_company(self):
        api_result = self.empoyee_api.get_without_company()
        assert api_result.status_code == 500

    @allure.id('empl_3')
    @allure.story('Добавление сотрудника со всеми полями')
    @allure.title('Добавить сотрудника с передачей всех полей')
    @allure.description('Добавление нового сотрудника с заполнением информации по всем полям')
    @allure.feature('CREATE')
    @pytest.mark.parametrize(
        'company_name, ' +
        'first_name, ' +
        'last_name, ' +
        'middle_name, ' +
        'email, ' +
        'url, ' +
        'phone, ' +
        'birthdate, ' +
        'username, ' +
        'password, ', 
      [
          (
              'Sky Pro', 
              'Petr', 
              'Ivanov', 
              'Ivanovich', 
              'test@mail.ru', 
              'https://test.com',
              '8 999 999 99 99',
              '1990-06-07',
              username, 
              password
          )
      ]
    )
    @pytest.mark.xfail
    def test_add_employee_all_field(
        self,
        company_name: str,  
        first_name: str,  
        last_name: str,  
        middle_name: str,  
        email: str,  
        url: str,  
        phone: str,  
        birthdate: str,  
        username: str,  
        password: str,
    ):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        
        employee_body = {
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
        }
        token = self.auth_api.get_token(username, password)
        api_result = self.empoyee_api.create(get_auth_header(token), body=employee_body)
        employee_id = api_result.json()['id']

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 201
        assert api_result.json().get('id', None) != None
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['company_id'] == company_id
        assert db_result['avatar_url'] == url
        assert db_result['phone'] == phone
        assert str(db_result['birthdate']) == birthdate
        assert db_result['is_active'] == True
        assert db_result['email'] == email

    @allure.id('empl_4')
    @allure.story('Добавление сотрудника с обязательными полями')
    @allure.title('Добавить сотрудника с передачей только обязательных полей')
    @allure.description('Добавление нового сотрудника с заполнением информации только обязательных полей')
    @allure.feature('CREATE')
    @pytest.mark.parametrize('company_name, first_name, last_name, phone, username, password', 
        [('Sky Pro', 'Petr', 'Ivanov', '7 999 344 5455', username, password)]
    )
    def test_add_employee_required_fields(self, company_name: str, first_name: str, last_name: str, phone: str, username: str, password: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        
        token = self.auth_api.get_token(username, password)
        employee_body = {
            'firstName': first_name,
            'lastName': last_name,
            'phone': phone,
            'companyId': company_id
        }
        api_result = self.empoyee_api.create(get_auth_header(token), body=employee_body)
        employee_id = api_result.json()['id']

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 201
        assert api_result.json().get('id', None) != None
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['company_id'] == company_id
        assert db_result['phone'] == phone
        assert db_result['is_active'] == True
        assert db_result['email'] == None
        assert db_result['birthdate'] == None
        assert db_result['middle_name'] == None
        assert db_result['avatar_url'] == None

    @allure.id('empl_5')
    @allure.story('Добавление сотрудника (негатив)')
    @allure.title('Проверка ответа на попытку добавления сотрудника без передачи body')
    @allure.description('Выполнение запроса на добавление нового сотрудника без передачи тела запроса (негативная проверка)')
    @allure.feature('CREATE') 
    @pytest.mark.parametrize('username, password', [(username, password)])
    def test_add_employee_without_body(self, username: str, password: str):  
        token = self.auth_api.get_token(username, password)
        api_result = self.empoyee_api.create_without_body(get_auth_header(token))
        assert api_result.status_code == 500
    
    @allure.id('empl_6')
    @allure.story('Добавление сотрудника (негатив)')
    @allure.title('Проверка ответа на попытку добавления сотрудника без передачи токена')
    @allure.description('Выполнение запроса на добавление нового сотрудника без авторизации (негативная проверка)')
    @allure.feature('CREATE')   
    @pytest.mark.parametrize('company_name, first_name, last_name, phone', [('Sky Pro', 'Petr', 'Ivanov', '7 999 344 5455')])
    def test_add_employee_without_auth(self, company_name: str, first_name: str, last_name: str, phone: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        employee_before = self.employee_db.get_employees_by_company(company_id)
        
        employee_body = {
            'firstName': first_name,
            'lastName': last_name,
            'phone': phone,
            'companyId': company_id
        }
        api_result = self.empoyee_api.create({}, body=employee_body)

        employee_after = self.employee_db.get_employees_by_company(company_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 401
        assert len(employee_before) == len(employee_after)

    @allure.id('empl_7')
    @allure.story('Получение информацию о сотруднике по id')
    @allure.title('Получить информацию о сотруднике по id')
    @allure.description('Получение информации о сотруднике по его id')
    @allure.feature('READ')
    @pytest.mark.parametrize('company_name, first_name, last_name, middle_name, email, url, phone, birthdate', 
        [('Company Test','Alex','Ivanov','Antonovich','test@mail.ru','https://test.com','8 999 999 99 99','1990-02-03')])
    def test_get_employee_by_id(self, company_name: str, first_name: str, last_name: str, middle_name: str, email: str, url: str, phone: str, birthdate: str,):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        employee_body = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'company_id': company_id,
            'phone': phone,
            'email': email,
            'avatar_url': url,
            'birthdate': birthdate,
            'company_id': company_id  
        }
        self.employee_db.create_with_all(employee_body)
        employee_id = self.employee_db.get_max_id()

        api_result = self.empoyee_api.get_by_id(employee_id)
        
        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 200
        assert api_result.json()['id'] == employee_id
        assert api_result.json()['firstName'] == first_name
        assert api_result.json()['lastName'] == last_name
        assert api_result.json()['middleName'] == middle_name
        assert api_result.json()['companyId'] == company_id
        assert api_result.json()['phone'] == phone
        assert api_result.json()['isActive'] == True
        assert api_result.json()['avatar_url'] == url
        assert api_result.json()['email'] == email
        assert api_result.json()['birthdate'] == str(birthdate)
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['company_id'] == company_id
        assert db_result['phone'] == phone
        assert db_result['avatar_url'] == url
        assert str(db_result['birthdate']) == birthdate
        assert db_result['is_active'] == True
        assert api_result.json()['email'] == email
        assert db_result['email'] == email

    @allure.id('empl_8')
    @allure.story('Получение информацию о сотруднике (негатив)')
    @allure.title('Проверка ответа на попытку получения информации о сотруднике без передачи id')
    @allure.description('Выполнение запроса на получения информации о сотруднике без передачи id (негативная проверка)')
    @allure.feature('READ')   
    def test_get_employee_without_id(self):
        api_result = self.empoyee_api.get_without_id()
        assert api_result.status_code == 500
    
    @allure.id('empl_9')
    @allure.story('Редактирование информации о сотруднике')
    @allure.title('Редактировать информацию о сотруднике')
    @allure.description('Обновление информации о сотруднике')
    @allure.feature('UPDATE')  
    @pytest.mark.parametrize(
        'company_name, ' +
        'first_name, ' +
        'last_name, ' +
        'middle_name, ' +
        'email, ' +
        'url, ' +
        'phone, ' +
        'birthdate, ' +
        'new_last_name, ' +
        'new_email, ' +
        'new_phone, ' +
        'new_url, ' +
        'username, ' +
        'password ', 
      [
          (
              'Company Test', 
              'Alex', 
              'Ivanov', 
              'Antonovich',
              'test@mail.ru', 
              'https://test.com',
              '8 999 999 99 99',
              '1990-02-03',
              'Artemov',
              'artemov@mail.com',
              '8 777 123 23 55',
              'https://artemov.test.com',
              username, 
              password
          )
      ]
    )
    @pytest.mark.xfail
    def test_edit_employee(
        self,
        company_name: str,  
        first_name: str,  
        last_name: str,
        middle_name: str, 
        email: str,  
        url: str,  
        phone: str, 
        birthdate: str, 
        new_last_name: str,  
        new_email: str,  
        new_phone: str,
        new_url: str,  
        username: str,  
        password: str,
    ):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        old_body = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'phone': phone,
            'email': email,
            'avatar_url': url,
            'birthdate': birthdate,
            'company_id': company_id  
        }
        self.employee_db.create_with_all(old_body)
        employee_id = self.employee_db.get_max_id()
        
        token = self.auth_api.get_token(username, password)
        edited_body = {
            'lastName': new_last_name,
            'email': new_email,
            'url': new_url,
            'phone': new_phone,
            'isActive': False
        }
        api_result = self.empoyee_api.edit(get_auth_header(token), employee_id, edited_body)

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 200
        assert api_result.json()['id'] == employee_id
        assert api_result.json()['email'] == new_email
        assert api_result.json()['url'] == new_url
        assert api_result.json()['isActive'] == False
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == new_last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['email'] == new_email
        assert db_result['company_id'] == company_id
        assert db_result['avatar_url'] == new_url
        assert db_result['is_active'] == False
        assert str(db_result['birthdate']) == birthdate
        assert db_result['phone'] == new_phone
   
    @allure.id('empl_10')
    @allure.story('Редактирование информации о сотруднике (негатив)')
    @allure.title('Проверка ответа на попытку редактирования сотрудника без передачи id')
    @allure.description('Выполнение запроса на обновление информации о сотруднике без передачи id (негативная проверка)')
    @allure.feature('UPDATE')     
    @pytest.mark.parametrize(
        'company_name, ' +
        'first_name, ' +
        'last_name, ' +
        'middle_name, ' +
        'email, ' +
        'url, ' +
        'phone, ' +
        'birthdate, ' +
        'new_last_name, ' +
        'new_email, ' +
        'new_phone, ' +
        'new_url, ' +
        'username, ' +
        'password ', 
      [
          (
              'Company Test', 
              'Alex', 
              'Ivanov', 
              'Antonovich',
              'test@mail.ru', 
              'https://test.com',
              '8 999 999 99 99',
              '1990-02-03',
              'Artemov',
              'artemov@mail.com',
              '8 777 123 23 55',
              'https://artemov.test.com',
              username, 
              password
          )
      ]
    )
    def test_edit_employee_without_id(
        self,
        company_name: str,  
        first_name: str,  
        last_name: str,
        middle_name: str, 
        email: str,  
        url: str,  
        phone: str, 
        birthdate: str, 
        new_last_name: str,  
        new_email: str,  
        new_phone: str,
        new_url: str,  
        username: str,  
        password: str,
    ):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        old_body = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'phone': phone,
            'email': email,
            'avatar_url': url,
            'birthdate': birthdate,
            'company_id': company_id  
        }
        self.employee_db.create_with_all(old_body)
        employee_id = self.employee_db.get_max_id()
        
        token = self.auth_api.get_token(username, password)
        edited_body = {
            'lastName': new_last_name,
            'email': new_email,
            'url': new_url,
            'phone': new_phone,
            'isActive': False
        }
        api_result = self.empoyee_api.edit_without_id(get_auth_header(token), edited_body)

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 404
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['email'] == email
        assert db_result['company_id'] == company_id
        assert db_result['avatar_url'] == url
        assert db_result['is_active'] == True
        assert str(db_result['birthdate']) == birthdate
        assert db_result['phone'] == phone
     
    @allure.id('empl_11')
    @allure.story('Редактирование информации о сотруднике (негатив)')
    @allure.title('Проверка ответа на попытку редактирования сотрудника без body')
    @allure.description('Выполнение запроса на обновление информации о сотруднике без тела запроса (негативная проверка)')
    @allure.feature('UPDATE')   
    @pytest.mark.parametrize(
        'company_name, ' +
        'first_name, ' +
        'last_name, ' +
        'middle_name, ' +
        'email, ' +
        'url, ' +
        'phone, ' +
        'birthdate, ' +
        'username, ' +
        'password ', 
      [
          (
              'Company Test', 
              'Alex', 
              'Ivanov', 
              'Antonovich',
              'test@mail.ru', 
              'https://test.com',
              '8 999 999 99 99',
              '1990-02-03',
              username, 
              password
          )
      ]
    )
    def test_edit_employee_without_body(
        self,
        company_name: str,  
        first_name: str,  
        last_name: str,
        middle_name: str, 
        email: str,  
        url: str,  
        phone: str, 
        birthdate: str,  
        username: str,  
        password: str,
    ):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        old_body = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'phone': phone,
            'email': email,
            'avatar_url': url,
            'birthdate': birthdate,
            'company_id': company_id  
        }
        self.employee_db.create_with_all(old_body)
        employee_id = self.employee_db.get_max_id()
        
        token = self.auth_api.get_token(username, password)
        api_result = self.empoyee_api.edit_without_body(get_auth_header(token), employee_id)

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 200
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['email'] == email
        assert db_result['company_id'] == company_id
        assert db_result['avatar_url'] == url
        assert db_result['is_active'] == True
        assert str(db_result['birthdate']) == birthdate
        assert db_result['phone'] == phone
    
    @allure.id('empl_12')
    @allure.story('Редактирование информации о сотруднике (негатив)')
    @allure.title('Проверка ответа на попытку редактирования сотрудника без передачи токена')
    @allure.description('Выполнение запроса на обновление информации о сотруднике без авторизации (негативная проверка)')
    @allure.feature('UPDATE')   
    @pytest.mark.parametrize(
        'company_name, ' +
        'first_name, ' +
        'last_name, ' +
        'middle_name, ' +
        'email, ' +
        'url, ' +
        'phone, ' +
        'birthdate, ' +
        'new_last_name, ' +
        'new_email, ' +
        'new_phone, ' +
        'new_url, ', 
      [
          (
              'Company Test', 
              'Alex', 
              'Ivanov', 
              'Antonovich',
              'test@mail.ru', 
              'https://test.com',
              '8 999 999 99 99',
              '1990-02-03',
              'Artemov',
              'artemov@mail.com',
              '8 777 123 23 55',
              'https://artemov.test.com'
          )
      ]
    )
    def test_edit_employee_without_auth(
        self,
        company_name: str,  
        first_name: str,  
        last_name: str,
        middle_name: str, 
        email: str,  
        url: str,  
        phone: str, 
        birthdate: str, 
        new_last_name: str,  
        new_email: str,  
        new_phone: str,
        new_url: str
    ):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        old_body = {
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name,
            'phone': phone,
            'email': email,
            'avatar_url': url,
            'birthdate': birthdate,
            'company_id': company_id  
        }
        self.employee_db.create_with_all(old_body)
        employee_id = self.employee_db.get_max_id()
        
        edited_body = {
            'lastName': new_last_name,
            'email': new_email,
            'url': new_url,
            'phone': new_phone,
            'isActive': False
        }
        api_result = self.empoyee_api.edit({}, employee_id, edited_body)

        db_result = self.employee_db.get_employee_by_id(employee_id)
        self.employee_db.delete(employee_id)
        self.company_db.delete(company_id)
        
        assert api_result.status_code == 401
        assert db_result['id'] == employee_id
        assert db_result['first_name'] == first_name
        assert db_result['last_name'] == last_name
        assert db_result['middle_name'] == middle_name
        assert db_result['email'] == email
        assert db_result['company_id'] == company_id
        assert db_result['avatar_url'] == url
        assert db_result['is_active'] == True
        assert str(db_result['birthdate']) == birthdate
        assert db_result['phone'] == phone