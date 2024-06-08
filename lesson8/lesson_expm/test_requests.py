import requests

base_url = 'https://x-clients-be.onrender.com'

def test_get_companies():
  resp = requests.get(f'{base_url}/company')
  
  print(resp.json())
  first_company = resp.json()[0]
  
  assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
  assert resp.status_code == 200
  assert first_company['name'] == "Барбершоп 'ЦирюльникЪ'"
  
def test_login():
  creds = {
    "username": "michaelangelo",
    "password": "party-dude"
  } 
  resp = requests.post(f'{base_url}/auth/login', json=creds)
  
  token = resp.json()['userToken']
  assert resp.status_code == 201
  assert len(token) > 0
  
def test_add_company():
  creds = {
    "username": "bloom",
    "password": "fire-fairy"
  }   
  company = {
    "name": "sky1",
    "description": "testing1"
  }
  
  # authorization
  auth_resp = requests.post(f'{base_url}/auth/login', json=creds)
  token = auth_resp.json()['userToken']
  
  # add company
  my_headers = {}
  my_headers['x-client-token'] = token
  resp = requests.post(f'{base_url}/company', json=company, headers=my_headers)

  assert resp.status_code == 201
  assert resp.json()['id'] > 0
  
