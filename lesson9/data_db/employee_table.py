from sqlalchemy import create_engine, Engine, Connection, Sequence, RowMapping
from sqlalchemy  import text

class EmployeeTable:
  __db: Engine
  __connection: Connection
  
  def __init__(self, connection_str: str) -> None:
    self.__db = create_engine(connection_str)
    self.__connection = self.__db.connect()
    
  def get_employee_by_id(self, id: int)  -> RowMapping | None:
    sql = text('''
      select *
      from employee
      where id = :id;
    ''')
    res = self.__connection.execute(sql, {'id': id}).mappings().all()
    if len(res) == 1:
      return res[0]
    else:
      return None
    
  def get_employees_by_company(self, company_id: int) -> Sequence[RowMapping]:
    sql = text('select * from employee where company_id = :company_id')
    return self.__connection.execute(sql, {'company_id': company_id}).mappings().all()
  
  def delete(self, id: int) -> None:
    sql = text('''
      delete from employee
      where id = :id
    ''')
    self.__connection.execute(sql, {'id': id})
    self.__connection.commit()
    
  def create_with_required(self,  body: dict) -> None:
    sql = text('''
      insert into employee("first_name", "last_name", "phone", "company_id")
      values (:first_name, :last_name, :phone, :company_id)
    ''')
    self.__connection.execute(sql, {
      'first_name': body['first_name'],
      'last_name': body['last_name'], 
      'phone': body['phone'],
      'company_id': body['company_id']})
    self.__connection.commit()
    
  def create_with_all(self,  body: dict) -> None:
    sql = text('''
      insert into employee("first_name", "last_name", "middle_name", "phone", "email", "avatar_url", "birthdate", "company_id")
      values (:first_name, :last_name, :middle_name, :phone, :email, :avatar_url, :birthdate, :company_id)
    ''')
    self.__connection.execute(sql, {
      'first_name': body['first_name'],
      'last_name': body['last_name'], 
      'middle_name': body['middle_name'],
      'phone': body['phone'],
      'email': body['email'],
      'avatar_url': body['avatar_url'],
      'birthdate': body['birthdate'],
      'company_id': body['company_id']
    })
    self.__connection.commit()
      
  def get_max_id(self) -> int:
    sql = text('''
      select MAX(id) as id
      from employee
    ''')
    return self.__connection.execute(sql).mappings().all()[0]['id']
