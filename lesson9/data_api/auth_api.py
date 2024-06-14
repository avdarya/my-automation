import requests 

class AuthApi:
  base_url: str
  
  def __init__(self, base_url: str) -> None:
    self.base_url = base_url
    
  def get_token(self, username: str, password: str) -> str:
    body = {
      "username": username,
      "password": password
    }
    resp = requests.post(f'{self.base_url}/auth/login', json=body)
    return resp.json()['userToken']