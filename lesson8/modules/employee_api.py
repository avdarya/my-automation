import requests
from requests import Response

class EmployeeApi:
  base_url: str
  
  def __init__(self, base_url: str) -> None:
    self.base_url = base_url
    
  def get_by_company(self, company_id: int) -> Response:
    return requests.get(f'{self.base_url}/employee', params={'company': company_id})
  
  def create(self, headers: dict, body: dict) -> Response:
    return requests.post(f'{self.base_url}/employee', headers=headers, json=body)
  
  def get_by_id(self, employee_id: int) -> Response:
    return requests.get(f'{self.base_url}/employee/{employee_id}')
  
  def edit(self, headers: dict, id: int, body: dict) -> Response:
    return requests.patch(f'{self.base_url}/employee/{id}', headers=headers, json=body)