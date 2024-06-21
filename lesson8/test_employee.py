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

@pytest.mark.parametrize('company_name, first_name, last_name, phone, username, password', 
  [('Sky Pro', 'Petr', 'Ivanov', '8 999 999 99 99', username, password)]
)
def test_get_employees_by_company(company_name: str, first_name: str, last_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)

  empl_by_company = empoyee_api.get_by_company(company.json()['id'])
  
  assert empl_by_company.status_code == 200
  assert len(empl_by_company.json()) > 0
  assert empl_by_company.json()[-1]['id'] == employee.json()['id']

@pytest.mark.parametrize(
  'company_name, ' +
  'first_name, ' +
  'last_name, ' +
  'middle_name, ' +
  'email, ' +
  'url, ' +
  'phone, ' +
  'birthdate, ' +
  'is_active, ' +
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
      True,
      username, 
      password
    )
  ]
)
@pytest.mark.xfail
def test_add_employee_all_field(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  middle_name: str,  
  email: str,  
  url: str,  
  phone: str,  
  birthdate: str,  
  is_active: bool,  
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  res_before = empoyee_api.get_by_company(company.json()['id'])
  body_before = res_before.json()

  body = {
    'firstName': first_name,
    'lastName': last_name,
    'middleName': middle_name,
    'companyId': company.json()['id'],
    'email': email,
    'url': url,
    'phone': phone,
    'birthdate': birthdate,
    'isActive': is_active
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)

  res_after = empoyee_api.get_by_company(company.json()['id'])
  body_after = res_after.json()
  
  assert employee.status_code == 201
  assert employee.json().get('id', None) != None
  assert len(body_after) - len(body_before) == 1
  assert body_after[-1]['id'] == employee.json()['id']
  assert body_after[-1]['firstName'] == first_name
  assert body_after[-1]['lastName'] == last_name
  assert body_after[-1]['middleName'] == middle_name
  assert body_after[-1]['companyId'] == company.json()['id']
  assert body_after[-1]['avatar_url'] == url
  assert body_after[-1]['phone'] == phone
  assert body_after[-1]['birthdate'] == birthdate
  assert body_after[-1]['isActive'] == is_active
  assert body_after[-1]['email'] == email

@pytest.mark.parametrize('company_name, first_name, last_name, username, password', 
  [('Sky Pro', 'Petr', 'Ivanov', username, password)]
)
@pytest.mark.xfail
def test_add_employee_required_fields(company_name: str, first_name: str, last_name: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  res_before = empoyee_api.get_by_company(company.json()['id'])
  body_before = res_before.json()

  body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id']
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)

  res_after = empoyee_api.get_by_company(company.json()['id'])
  body_after = res_after.json()
  
  assert employee.status_code == 201
  assert employee.json().get('id', None) != None
  assert len(body_after) - len(body_before) == 1
  assert body_after[-1]['id'] == employee.json()['id']
  assert body_after[-1]['firstName'] == first_name
  assert body_after[-1]['lastName'] == last_name
  assert body_after[-1]['companyId'] == company.json()['id']
  assert body_after[-1]['middleName'] == None
  assert body_after[-1]['phone'] == None
  assert body_after[-1]['email'] == None
  assert body_after[-1]['birthdate'] == None
  assert body_after[-1]['avatar_url'] == None
  assert body_after[-1]['isActive'] == True

@pytest.mark.parametrize('company_name, last_name, phone, username, password', 
  [('Sky Eng', 'Fadeev', '8 919 912 68 44', username, password)]
)
def test_add_employee_whiout_first_name(company_name: str, last_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  body = {
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)
  
  assert employee.status_code == 500
  
@pytest.mark.parametrize('company_name, first_name, phone, username, password', 
  [('Sky Pro', 'Petr', '8 919 912 68 44', username, password)]
)
def test_add_employee_whiout_last_name(company_name: str, first_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)
  
  body = {
    'firstName': first_name,
    'companyId': company.json()['id'],
    'phone': phone
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)
  
  assert employee.status_code == 500
  
@pytest.mark.parametrize('first_name, last_name, phone, username, password', 
  [('Petr', 'Ivanov', '8 999 202 33 23', username, password)]
)
def test_add_employee_without_company_id(first_name: str, last_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  
  body = {
    'firstName': first_name,
    'lastName': last_name,
    'phone': phone
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)
  
  assert employee.status_code == 500
  
@pytest.mark.parametrize('company_name, first_name, last_name, phone, username, password', 
  [('Python', 'Misha', 'Pertov', '8 912 354 12 44', username, password)]
)
def test_get_employee_by_id(company_name: str, first_name: str, last_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone
  }
  employee = empoyee_api.create(get_auth_header(token), body=body)

  empl_by_id = empoyee_api.get_by_id(employee.json()['id'])

  assert empl_by_id.status_code == 200
  assert empl_by_id.json()['id'] == employee.json()['id']
  assert empl_by_id.json()['firstName'] == first_name
  assert empl_by_id.json()['lastName'] == last_name
  assert empl_by_id.json()['companyId'] == company.json()['id']
  assert empl_by_id.json()['phone'] == phone

@pytest.mark.parametrize(
  'company_name, ' +
  'first_name, ' +
  'last_name, ' +
  'email, ' +
  'url, ' +
  'phone, ' +
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
      'test@mail.ru', 
      'https://test.com',
      '8 999 999 99 99',
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
def test_edit_employee_all_fields(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  email: str,  
  url: str,  
  phone: str,  
  new_last_name: str,  
  new_email: str,  
  new_phone: str,
  new_url: str,  
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'email': email,
    'url': url,
    'phone': phone
}
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {
    'lastName': new_last_name,
    'email': new_email,
    'url': new_url,
    'phone': new_phone,
    'isActive': False
  }
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert edited_employee.status_code == 200
  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['lastName'] == new_last_name
  assert employee_by_id.json()['email'] == new_email
  assert employee_by_id.json()['avatar_url'] == new_url
  assert employee_by_id.json()['isActive'] == False
  assert employee_by_id.json()['phone'] == new_phone

@pytest.mark.parametrize('company_name, first_name, last_name, phone, new_last_name, username, password', 
  [('Company Test', 'Alex', 'Ivanov', '8 999 999 99 99', 'Voronov', username, password)]
)
@pytest.mark.xfail
def test_edit_employee_last_name(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  phone: str,  
  new_last_name: str,  
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone
  }
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {'lastName': new_last_name}
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['lastName'] == new_last_name
  assert employee_by_id.json()['phone'] == phone
  assert employee_by_id.json()['companyId'] == company.json()['id']
  assert edited_employee.status_code == 201

@pytest.mark.parametrize('company_name, first_name, last_name, email, phone, new_email, username, password', 
  [('Company Test', 'Alex', 'Ivanov', 'ivanov@mail.ru', '8 999 999 99 99', 'new_ivanov@mail.ru', username, password)]
)
@pytest.mark.xfail
def test_edit_employee_email(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  email: str,  
  phone: str,  
  new_email: str, 
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'email': email,
    'phone': phone
  }
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {'email': new_email}
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['email'] == new_email
  assert employee_by_id.json()['lastName'] == last_name
  assert employee_by_id.json()['phone'] == phone
  assert employee_by_id.json()['companyId'] == company.json()['id']
  assert edited_employee.status_code == 201

@pytest.mark.parametrize('company_name, first_name, last_name, url, phone, new_url, username, password',
  [('Company Test', 'Alex', 'Ivanov', 'https://ivanov.ru', '8 999 999 99 99', 'https://test-ivanov.ru', username, password)]
)
@pytest.mark.xfail
def test_edit_employee_url(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  url: str,  
  phone: str, 
  new_url: str,  
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'url': url,
    'phone': phone
  }
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {'url': new_url}
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['avatar_url'] == new_url
  assert employee_by_id.json()['lastName'] == last_name
  assert employee_by_id.json()['phone'] == phone
  assert employee_by_id.json()['companyId'] == company.json()['id']
  assert edited_employee.status_code == 201

@pytest.mark.parametrize('company_name, first_name, last_name, phone, new_phone, username, password', 
  [('Company Test', 'Alex', 'Ivanov', '8 999 999 99 99', '8 912 354 34 32', username, password)]
)
@pytest.mark.xfail
def test_edit_employee_phone(
  company_name: str,  
  first_name: str,  
  last_name: str,  
  phone: str,  
  new_phone: str,
  username: str,  
  password: str,
):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone
}
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {'phone': new_phone}
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['phone'] == new_phone
  assert employee_by_id.json()['lastName'] == last_name
  assert employee_by_id.json()['companyId'] == company.json()['id']
  assert edited_employee.status_code == 201

@pytest.mark.parametrize('company_name, first_name, last_name, phone, username, password', 
  [('Company Test', 'Alex', 'Ivanov', '8 912 354 34 32', username, password)]
)
@pytest.mark.xfail
def test_edit_employee_status(company_name: str, first_name: str, last_name: str, phone: str, username: str, password: str):
  token = auth_api.get_token(username, password)
  company = company_api.create_company(get_auth_header(token), company_name)

  old_body = {
    'firstName': first_name,
    'lastName': last_name,
    'companyId': company.json()['id'],
    'phone': phone,
    'isActive': True
}
  old_employee = empoyee_api.create(get_auth_header(token), body=old_body)

  edited_body = {'isActive': False}
  edited_employee = empoyee_api.edit(get_auth_header(token), old_employee.json()['id'], edited_body)

  employee_by_id = empoyee_api.get_by_id(edited_employee.json()['id'])

  assert employee_by_id.json()['id'] == edited_employee.json()['id']
  assert employee_by_id.json()['phone'] == phone
  assert employee_by_id.json()['lastName'] == last_name
  assert employee_by_id.json()['companyId'] == company.json()['id']
  assert employee_by_id.json()['isActive'] == False
  assert edited_employee.status_code == 201