from sqlalchemy import create_engine, Engine, Connection, Sequence, RowMapping
from sqlalchemy  import text

class CompanyTable:
  __db: Engine
  
  def __init__(self, connection_str: str) -> None:
    self.__db = create_engine(connection_str)
    
  def get_companies(self) -> Sequence[RowMapping]:
    try:
      with self.__db.connect() as conn:
        result = conn.execute(text('select * from company where deleted_at isnull')).mappings().all()
        return result
    except Exception as _ex:
      print('[INFO] Error - can\'t work with SQL ' , _ex)
    finally:
      if conn:
        conn.close()
        
  
  def get_active_companies(self) -> Sequence[RowMapping]:
    with self.__db.connect() as conn:
      result = conn.execute(text('select * from company where deleted_at isnull and is_active = true')).mappings().all()
      return result
  
  def get_company_by_id(self, id: int) -> RowMapping | None:
    sql = text('''
      select *
      from company
      where id = :id and deleted_at isnull
    ''')
    with self.__db.connect() as conn:
      result = conn.execute(sql, {'id': id}).mappings().all()
      if len(result) == 1:
        return result[0]
      else:
        return None
  
  def create(self,  name: str, description: str = '') -> None:
    sql = text('''
      insert into company ("name", "description")
      values (:name, :description)
    ''')
    with self.__db.connect() as conn:
      conn.execute(sql, {'name': name, 'description': description})
      conn.commit()
  
  def delete(self, id: int) -> None:
    sql = text('''
      delete from company
      where id = :id
    ''')
    with self.__db.connect() as conn:
      conn.execute(sql, {'id': id})
      conn.commit()
    
  def get_max_id(self) -> int:
    sql = text('''
      select MAX(id) as id
      from company
    ''')
    with self.__db.connect() as conn:
      result = conn.execute(sql).mappings().all()[0]['id']
      return result
