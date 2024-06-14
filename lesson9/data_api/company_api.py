import requests
from requests import Response

class CompanyApi:
  base_url: str
  
  def __init__(self, base_url: str) -> None:
    self.base_url = base_url
    
  def create_company(self,  headers: dict, name: str, description: str = '') -> Response:
    body = {
      "name": name,
      "description": description
    }
    return requests.post(f'{self.base_url}/company', headers=headers, json=body)
    
  def get_company_list(self, params: dict | None = None) -> Response:
    return requests.get(f'{self.base_url}/company', params=params)
  
  def get_company_by_id(self, id: int) -> Response:
    return requests.get(f'{self.base_url}/company/{str(id)}')
  
  def edit_company(self, headers: dict, id: int, name: str, descr: str) -> Response:
    body = {
      'name': name,
      'description': descr
    }
    return requests.patch(f'{self.base_url}/company/{str(id)}', headers=headers, json=body)
  
  def delete_company(self, headers: dict, id: int) -> Response:
    return requests.get(f'{self.base_url}/company/delete/{str(id)}', headers=headers)
  
  def set_status(self, headers: dict, id: int, is_active: bool) -> Response:
    return requests.patch(f'{self.base_url}/company/status/{str(id)}', headers=headers, json={"isActive": is_active})