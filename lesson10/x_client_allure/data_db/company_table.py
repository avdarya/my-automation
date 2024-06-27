import allure
from sqlalchemy import create_engine, Engine, Connection, Sequence, RowMapping
from sqlalchemy  import text

class CompanyTable:
    """Класс предоставляет методы для отправки SQL-запросов в БД приложения по компаниям"""
    
    __db: Engine
    
    def __init__(self, connection_str: str) -> None:
        """
            Создание экземпляра класса CompanyTable
            :param connection_str(str): строка подключения к БД
            
            :return: None
        """
        
        self.__db = create_engine(connection_str)
      
    @allure.step('bd. Получить список компаний')
    def get_companies(self) -> Sequence[RowMapping]:
        """
            Получение списка компаний
            
            :return: Sequence[RowMapping]: все скалярные значения в списке
        """
        
        try:
            with self.__db.connect() as conn:
                query = conn.execute(text('select * from company where deleted_at isnull'))
                result = query.mappings().all()
                allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
                return result
        except Exception as _ex:
            print('[INFO] Error - can\'t work with SQL ' , _ex)
        finally:
            if conn:
                conn.close()
      
    @allure.step('bd. Получить список активных компаний')    
    def get_active_companies(self) -> Sequence[RowMapping]:
        """
            Получение списка активных компаний
            
            :return: Sequence[RowMapping]: все скалярные значения в списке
        """
        
        with self.__db.connect() as conn:
            query = conn.execute(text('select * from company where deleted_at isnull and is_active = true'))
            result = query.mappings().all()
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.close()
            return result
    
    @allure.step('bd. Получить компанию по id {id}')
    def get_company_by_id(self, id: int) -> RowMapping | None:
        """
            Получение компании по id
            :param id(int): id компании
            
            :return: RowMapping | None: объект RowMapping или None 
        """
        
        sql = text('''
            select *
            from company
            where id = :id and deleted_at isnull
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'id': id})
            result = query.mappings().all()
            conn.close()
            if len(result) == 1:
                allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
                return result[0]
            else:
                return None
    
    @allure.step('bd. Создать компанию с названием {name} ({description})')
    def create(self,  name: str, description: str = '') -> None:
        """
            Создание компании
            :param name(str): название компании
            :param description(int): (optional) описание компании
            
            :return: None 
        """
        
        sql = text('''
            insert into company ("name", "description")
            values (:name, :description)
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'name': name, 'description': description})
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.commit()
            conn.close()
    
    @allure.step('bd. Удалить компанию')
    def delete(self, id: int) -> None:
        """
            Удаление компании
            :param id(int): id компании
            
            :return: None 
        """
        
        sql = text('''
            delete from company
            where id = :id
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'id': id})
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.commit()
            conn.close()
    
    @allure.step('bd. Получить max id компании')  
    def get_max_id(self) -> int:
        """
            Получение максимального id компании в БД
            
            :return: int: id компании
        """
        
        sql = text('''
            select MAX(id) as id
            from company
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql)
            result = query.mappings().all()[0]['id']
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.close()
            return result
