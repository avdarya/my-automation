import pytest
import allure
from data_api.company_api import CompanyApi
from data_api.auth_api import AuthApi
from data_api.employee_api import EmployeeApi
from data_db.company_table import CompanyTable
from get_auth_header import get_auth_header

@allure.epic('x-client Компании')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('Тесты на API-запросы компании')
class CompanyTest:
  
    base_url = 'https://x-clients-be.onrender.com'
    username = 'bloom'
    password = 'fire-fairy'
    database_connection_str = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

    auth_api = AuthApi(base_url)
    company_api = CompanyApi(base_url)
    company_db = CompanyTable(database_connection_str)

    @allure.id('comp_1')
    @allure.story('Получение компаний')
    @allure.title('Получить список компаний')
    @allure.description('Получение списка компаний')
    @allure.feature('READ')
    def test_get_companies(self):
        # with allure.step('Получить список компаний по API'):
        #     api_result = self.company_api.get_company_list()
        # with allure.step('Получить список компаний из БД'):
        #     db_result = self.company_db.get_companies()
            
        # with allure.step('Проверка:'):
        #     with allure.step('Статус-код 200'):
        #         assert api_result.status_code == 200
        #     with allure.step('Длина списков равна'):
        #         assert len(api_result.json()) == len(db_result)
  
        api_result = self.company_api.get_company_list()
        
        db_result = self.company_db.get_companies()
            
        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Длина списков равна'):
                assert len(api_result.json()) == len(db_result)

    @allure.id('comp_2')
    @allure.story('Получение активных компаний')
    @allure.title('Получить список активных компаний')
    @allure.description('Получение организации с параметом active = true')
    @allure.feature('READ')   
    def test_get_active_companies(self):
        api_result = self.company_api.get_company_list({'active': True})
        db_result = self.company_db.get_active_companies()
       
        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Длина списков равна:'):
                assert len(api_result.json()) == len(db_result)

    @allure.id('comp_3')
    @allure.story('Создание компании')
    @allure.title('Создать компанию')
    @allure.description('Добавление новой компании')
    @allure.feature('CREATE')
    @pytest.mark.parametrize('company_name, descr, username, password', [('Sky', 'Sky about', username, password)])
    def test_add_company(self, company_name: str, descr: str, username: str, password: str):
        res_before = self.company_api.get_company_list()
        body_before = res_before.json() 
          
        token = self.auth_api.get_token(username, password)
        new_company = self.company_api.create_company(get_auth_header(token), company_name, descr)
        new_id = new_company.json()['id']
            
        res_after = self.company_api.get_company_list()
        body_after = res_after.json()

        db_company = self.company_db.get_company_by_id(new_id)
        self.company_db.delete(new_id)

        with allure.step('Проверка:'):
            with allure.step('Статус-код 201'):
                assert new_company.status_code == 201
            with allure.step('Корректность значений полей компании в response body'):
                assert new_company.json().get('id', None) != None
                assert len(body_after) - len(body_before) == 1
                for company in body_after:
                    if company['id'] == new_id:
                      assert body_after[-1]['id'] == new_id
                      assert body_after[-1]['name'] == company_name
                      assert body_after[-1]['description'] == descr
                      assert body_after[-1]['isActive'] == True
            with allure.step('Корректность заполнения полей компании в БД'):
                assert db_company['id'] == new_id
                assert db_company['name'] == company_name
                assert db_company['description'] == descr
                assert db_company['is_active'] == True

    @allure.id('comp_4')
    @allure.story('Получение компании по id')
    @allure.title('Получить компанию по id')
    @allure.description('Получение конкретной компании по ее id')
    @allure.feature('READ')
    @pytest.mark.parametrize('company_name, descr', [('vs code', 'about vs code')])
    def test_get_company_by_id(self, company_name: str, descr: str):
        self.company_db.create(company_name, descr)
        company_id = self.company_db.get_max_id()

        api_result = self.company_api.get_company_by_id(company_id)

        self.company_db.delete(company_id)

        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Корректность значений полей компании в response body'):
                assert api_result.json()['id'] == company_id
                assert api_result.json()['name'] == company_name
                assert api_result.json()['description'] == descr

    @allure.id('comp_5')
    @allure.story('Редактирование компании')
    @allure.title('Редактировать компанию')
    @allure.description('Обновлении данных по компании')
    @allure.feature('UPDATE')   
    @pytest.mark.parametrize('old_name, old_descr, new_name, new_descr, username, password', 
       [('initial name', 'initial descr', 'edited name', 'edited descr', username, password)])
    def test_edit_company(self, old_name: str, old_descr: str, new_name: str, new_descr: str, username: str, password: str):
        self.company_db.create(old_name, old_descr)
        company_id = self.company_db.get_max_id()

        token = self.auth_api.get_token(username, password) 
        api_result = self.company_api.edit_company(get_auth_header(token), company_id, new_name, new_descr)
            
        company_result = self.company_db.get_company_by_id(company_id)
        self.company_db.delete(company_id)
      
        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Корректность значений полей компании в response body'):
                assert api_result.json()['id'] == company_id
                assert api_result.json()['name'] == new_name
                assert api_result.json()['description'] == new_descr
            with allure.step('Корректность заполнения полей компании в БД'):
                assert company_result['id'] == company_id 
                assert company_result['name'] == new_name
                assert company_result['description'] == new_descr

    @allure.id('comp_6')
    @allure.story('Удаление компании')
    @allure.title('Удалить компанию')
    @allure.description('Удаление компании')
    @allure.feature('DELETE')
    @pytest.mark.parametrize('company_name, username, password', [('Sky pro', username, password)])
    def test_delete_company(self, company_name: str, username: str, password: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()

        token = self.auth_api.get_token(username, password)
        api_result = self.company_api.delete_company(get_auth_header(token), company_id)

        self.company_db.get_companies() # for pause
        db_result = self.company_db.get_company_by_id(company_id)
        self.company_db.delete(company_id)
            
        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Корректность значений полей компании в response body'):
                assert api_result.json()['id'] == company_id
                assert api_result.json()['name'] == company_name
                assert api_result.json()['description'] == ''
            with allure.step('Отсутствие в БД компании, удаленной через API, c полем deleted_at == None'):
                assert db_result == None

    @allure.id('comp_7')
    @allure.story('Деактивация компании')
    @allure.title('Деактивировать компанию')
    @allure.description('Изменение статуса компании на isActive = False')
    @allure.feature('UPDATE')
    @pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
    def test_deactivated_company(self, company_name: str, username: str, password: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
        
        token = self.auth_api.get_token(username, password)
        api_result = self.company_api.set_status(get_auth_header(token), company_id, False)
                
        db_result = self.company_db.get_company_by_id(company_id)
        self.company_db.delete(company_id)

        with allure.step('Проверка:'):
            with allure.step('Статус-код 200'):
                assert api_result.status_code == 200
            with allure.step('Корректность статуса компании в response body'):
                assert api_result.json()['isActive'] == False
            with allure.step('Корректность статуса компании в БД'):
                assert db_result['id'] == company_id 
                assert db_result['is_active'] == False

    @allure.id('comp_8')
    @allure.story('Активация компании')
    @allure.title('Активаировать компанию')
    @allure.description('Изменение статуса компании на isActive = True')
    @allure.feature('UPDATE')
    @pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
    def test_activated_company(self, company_name: str, username: str, password: str):
        self.company_db.create(company_name)
        company_id = self.company_db.get_max_id()
          
        token = self.auth_api.get_token(username, password)
        self.company_api.set_status(get_auth_header(token), company_id, False)
        api_result = self.company_api.set_status(get_auth_header(token), company_id, True)
                
        db_result = self.company_db.get_company_by_id(company_id)
        self.company_db.delete(company_id)
       
        with allure.step('Проверка:'):
              with allure.step('Статус-код 200'):
                  assert api_result.status_code == 200
              with allure.step('Корректность статуса компании в response body'):
                  assert api_result.json()['isActive'] == True
              with allure.step('Корректность статуса компании в БД'):
                  assert db_result['id'] == company_id 
                  assert db_result['is_active'] == True 