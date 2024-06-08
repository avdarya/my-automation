import pytest
from modules.employee_api import EmployeeApi
from modules.auth_api import AuthApi
from modules.company_api import CompanyApi
from get_auth_header import get_auth_header


base_url = 'https://x-clients-be.onrender.com'
username = 'bloom'
password = 'fire-fairy'

auth_api = AuthApi(base_url)
company_api = CompanyApi(base_url)
empoyee_api = EmployeeApi(base_url)

@pytest.mark.parametrize('company_name, descr, username, password', [('Sky', 'Sky about', username, password)])
def test_add_company(company_name: str, descr: str, username: str, password: str):
  res_before = company_api.get_company_list()
  body_before = res_before.json()
  
  token = auth_api.get_token(username, password)
  new_company = company_api.create_company(get_auth_header(token), company_name, descr)
  new_id = new_company.json()['id']
  
  res_after = company_api.get_company_list()
  body_after  = res_after.json()
  
  assert new_company.status_code == 201
  assert new_company.json().get('id', None) != None
  assert len(body_after) - len(body_before) == 1
  assert body_after[-1]['id'] == new_id
  assert body_after[-1]['name'] == company_name
  assert body_after[-1]['description'] == descr
  assert body_after[-1]['isActive'] == True

@pytest.mark.parametrize('company_name, username, password', [('Sky pro', username, password)])
def test_get_companies(company_name: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  new_company = company_api.create_company(get_auth_header(token), company_name)
  result = company_api.get_company_list()
  body = result.json()
  
  assert result.status_code == 200
  assert len(body) > 0
  assert body[-1].get('id') == new_company.json().get('id')
  
@pytest.mark.parametrize('company_name, username, password', [('Sky active', username, password)])
def test_get_active_companies(company_name: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company_api.create_company(get_auth_header(token), company_name)
  
  result = company_api.get_company_list({'active': True})
  body = result.json()
  statuses = [bool]
  for comp in body:
    statuses.append(comp['isActive']) 

  assert result.status_code == 200
  assert len(body) > 0
  assert not False in statuses
  
@pytest.mark.parametrize('company_name, descr, username, password', [('vs code', 'about vs code', username, password)])
def test_get_company_by_id(company_name: str, descr: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name, descr)

  result = company_api.get_company_by_id(company.json()['id'])

  assert result.status_code == 200
  assert company.json()['id'] == result.json()['id']
  assert result.json()['name'] == company_name
  assert result.json()['description'] == descr

@pytest.mark.parametrize('old_name, old_descr, new_name, new_descr, username, password', 
  [('initial name', 'initial descr', 'edited name', 'edited descr', username, password)])
def test_edit_company(old_name: str, old_descr: str, new_name: str, new_descr: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), old_name, old_descr)
  
  edited_company = company_api.edit_company(get_auth_header(token), company.json()['id'], new_name, new_descr)
  
  assert edited_company.status_code == 200
  assert company.json()['id'] == edited_company.json()['id']
  assert new_name == edited_company.json()['name']
  assert new_descr == edited_company.json()['description']

@pytest.mark.parametrize('company_name, descr, username, password', [('requests', 'about', username, password)])
def test_delete_company(company_name: str, descr: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name, descr)

  deleted_company = company_api.delete_company(get_auth_header(token), company.json()['id'])
  
  company_api.get_company_list() # for pause
  companies = company_api.get_company_list()
  
  assert deleted_company.status_code == 200
  assert deleted_company.json()['id'] == company.json()['id']
  assert deleted_company.json()['name'] == company_name
  assert deleted_company.json()['description'] == descr
  assert companies.json()[-1]['id'] != deleted_company.json()['id']
  
@pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
def test_deactivated_company(company_name: str, username: str, password: str):
  status = False
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)
    
  deactivated_company = company_api.set_status(get_auth_header(token), company.json()['id'], status)
  
  assert deactivated_company.status_code == 200
  assert deactivated_company.json()['isActive'] == status
  
@pytest.mark.parametrize('company_name, username, password', [('requests', username, password)])
def test_activated_company(company_name: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)
  company_api.set_status(get_auth_header(token),  company.json()['id'], False)
  
  activated_company = company_api.set_status(get_auth_header(token),  company.json()['id'], True)

  assert activated_company.status_code == 200
  assert activated_company.json()['isActive'] == True 