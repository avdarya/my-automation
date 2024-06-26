import pytest
from data_api.company_api import CompanyApi
from data_api.auth_api import AuthApi
from data_api.employee_api import EmployeeApi
from data_db.company_table import CompanyTable
from get_auth_header import get_auth_header
 
base_url = 'https://x-clients-be.onrender.com'
username = 'bloom'
password = 'fire-fairy'
database_connection_str = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

auth_api = AuthApi(base_url)
company_api = CompanyApi(base_url)
company_db = CompanyTable(database_connection_str)

def test_get_companies(self):
  api_result = self.company_api.get_company_list()
  db_result = self.company_db.get_companies()
  assert api_result.status_code == 200
  assert len(api_result.json()) == len(db_result)

def test_get_active_companies():
  api_result = company_api.get_company_list({'active': True})
  db_result = company_db.get_active_companies()
  assert api_result.status_code == 200
  assert len(api_result.json()) == len(db_result)
    
@pytest.mark.parametrize('company_name, descr, username, password', [('Sky', 'Sky about', username, password)])
def test_add_company(company_name: str, descr: str, username: str, password: str):
  res_before = company_api.get_company_list()
  body_before = res_before.json()
    
  token = auth_api.get_token(username, password)
  new_company = company_api.create_company(get_auth_header(token), company_name, descr)
  new_id = new_company.json()['id']
      
  res_after = company_api.get_company_list()
  body_after  = res_after.json()
    
  db_company = company_db.get_company_by_id(new_id)
    
  company_db.delete(new_id)

  assert new_company.status_code == 201
  assert new_company.json().get('id', None) != None
  assert len(body_after) - len(body_before) == 1
  for company in body_after:
    if company['id'] == new_id:
      assert body_after[-1]['id'] == new_id
      assert body_after[-1]['name'] == company_name
      assert body_after[-1]['description'] == descr
      assert body_after[-1]['isActive'] == True
  assert db_company['id'] == new_id
  assert db_company['name'] == company_name
  assert db_company['description'] == descr
  assert db_company['is_active'] == True

@pytest.mark.parametrize('company_name, descr', [('vs code', 'about vs code')])
def test_get_company_by_id(company_name: str, descr: str):
  company_db.create(company_name, descr)
  company_id = company_db.get_max_id()
    
  api_result = company_api.get_company_by_id(company_id)
    
  company_db.delete(company_id)
    
  assert api_result.status_code == 200
  assert api_result.json()['id'] == company_id
  assert api_result.json()['name'] == company_name
  assert api_result.json()['description'] == descr
   
@pytest.mark.parametrize('old_name, old_descr, new_name, new_descr, username, password', 
  [('initial name', 'initial descr', 'edited name', 'edited descr', username, password)])
def test_edit_company(old_name: str, old_descr: str, new_name: str, new_descr: str, username: str, password: str):
  company_db.create(old_name, old_descr)
  company_id = company_db.get_max_id()
    
  token = auth_api.get_token(username, password)  
  api_result = company_api.edit_company(get_auth_header(token), company_id, new_name, new_descr)
    
  company_result = company_db.get_company_by_id(company_id)
    
  company_db.delete(company_id)
    
  assert api_result.status_code == 200
  assert api_result.json()['id'] == company_id
  assert api_result.json()['name'] == new_name
  assert api_result.json()['description'] == new_descr
  assert company_result['id'] == company_id 
  assert company_result['name'] == new_name
  assert company_result['description'] == new_descr
    
@pytest.mark.parametrize('company_name, username, password', [('Sky pro', username, password)])
def test_delete_company(company_name: str, username: str, password: str):
  company_db.create(company_name)
  company_id = company_db.get_max_id()
    
  token = auth_api.get_token(username, password)
  api_result = company_api.delete_company(get_auth_header(token), company_id)

  company_db.delete(company_id)
    
  assert api_result.status_code == 200
  assert api_result.json()['id'] == company_id
  assert api_result.json()['name'] == company_name
  assert api_result.json()['description'] == ''

@pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
def test_deactivated_company(company_name: str, username: str, password: str):
  company_db.create(company_name)
  company_id = company_db.get_max_id()
    
  token = auth_api.get_token(username, password)
  api_result = company_api.set_status(get_auth_header(token), company_id, False)
    
  db_result = company_db.get_company_by_id(company_id)
  company_db.delete(company_id)
    
  assert api_result.status_code == 200
  assert api_result.json()['isActive'] == False
  assert db_result['id'] == company_id 
  assert db_result['is_active'] == False

@pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
def test_activated_company(company_name: str, username: str, password: str):
  company_db.create(company_name)
  company_id = company_db.get_max_id()
    
  token = auth_api.get_token(username, password)
  company_api.set_status(get_auth_header(token), company_id, False)
    
  api_result = company_api.set_status(get_auth_header(token), company_id, True)
    
  db_result = company_db.get_company_by_id(company_id)
  company_db.delete(company_id)

  assert api_result.status_code == 200
  assert api_result.json()['isActive'] == True
  assert db_result['id'] == company_id 
  assert db_result['is_active'] == True 