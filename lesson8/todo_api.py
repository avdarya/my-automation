import requests
from requests import Response

class TodoApi:
  base_url: str
  
  def __init__(self, base_url: str) -> None:
    self.base_url = base_url
    
  def add_todo(self, title: str) -> Response:
    return requests.post(self.base_url, json={'title': title})
  
  def edit_title(self, id: int, title: str) -> Response:
    return requests.patch(f'{self.base_url}/{id}', json={'title': title})
  
  def delete_todo(self, id: int) -> Response:
    return requests.delete(f'{self.base_url}/{id}')
  
  def get_todo_list(self) -> Response:
    return requests.get(self.base_url)
  
  def get_todo_by_id(self, id: int) -> Response:
    return requests.get(f'{self.base_url}/{id}')
   
  def set_status(self, id: int, status: bool) -> Response:
    return requests.patch(f'{self.base_url}/{id}', json={'completed': status})