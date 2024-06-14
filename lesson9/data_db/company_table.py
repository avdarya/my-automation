from sqlalchemy import create_engine, Engine, Connection, Sequence, RowMapping
from sqlalchemy  import text

class CompanyTable:
  __db: Engine
  __connection: Connection
  
  def __init__(self, connection_str: str) -> None:
    self.__db = create_engine(connection_str)
    self.__connection = self.__db.connect()
    
  def get_companies(self) -> Sequence[RowMapping]:
    return self.__connection.execute(text('select * from company where deleted_at isnull')).mappings().all()
  
  def get_active_companies(self) -> Sequence[RowMapping]:
    return self.__connection.execute(text('select * from company where deleted_at isnull and is_active = true')).mappings().all()
  
  def get_company_by_id(self, id: int) -> RowMapping | None:
    sql = text('''
      select *
      from company
      where id = :id and deleted_at isnull
    ''')
    res = self.__connection.execute(sql, {'id': id}).mappings().all()
    if len(res) == 1:
      return res[0]
    else:
      return None
  
  def create(self,  name: str, description: str = '') -> None:
    sql = text('''
      insert into company ("name", "description")
      values (:name, :description)
    ''')
    self.__connection.execute(sql, {'name': name, 'description': description})
    self.__connection.commit()
  
  def delete(self, id: int) -> None:
    sql = text('''
      delete from company
      where id = :id
    ''')
    self.__connection.execute(sql, {'id': id})
    self.__connection.commit()
    
  def get_max_id(self) -> int:
    sql = text('''
      select MAX(id) as id
      from company
    ''')
    return self.__connection.execute(sql).mappings().all()[0]['id']
