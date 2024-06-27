import allure
from sqlalchemy import create_engine, Engine, Connection, Sequence, RowMapping
from sqlalchemy  import text

class EmployeeTable:
    """Класс предоставляет методы для отправки SQL-запросов в БД приложения по сотрудникам"""
    
    __db: Engine
    __connection: Connection
    
    def __init__(self, connection_str: str) -> None:
        """
            Создание экземпляра класса EmployeeTable
            :param connection_str(str): строка подключения к БД
            
            :return: None
        """
        
        self.__db = create_engine(connection_str)
        self.__connection = self.__db.connect()
    
    @allure.step('bd. Получить сотрудника по id {id}')
    def get_employee_by_id(self, id: int)  -> RowMapping | None:
        """
            Получение сотрудника по id
            :param id(int): id сотрудника
            
            :return: RowMapping | None: объект RowMapping или None 
        """
      
        sql = text('''
            select *
            from employee
            where id = :id;
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'id': id})
            res = query.mappings().all()
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.close()
            if len(res) == 1:
                return res[0]
            else:
                return None
    
    @allure.step('bd. Получить сотрудников в компании с id {company_id}')
    def get_employees_by_company(self, company_id: int) -> Sequence[RowMapping]:
        """
            Получение списка сотрудников компании
            :param company_id(int): id компании
            
            :return: Sequence[RowMapping]: все скалярные значения в списке
        """
      
        sql = text('select * from employee where company_id = :company_id')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'company_id': company_id})
            result = query.mappings().all()
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.close()
            return result
    
    @allure.step('bd. Удалить сотрудника')
    def delete(self, id: int) -> None:
        """
            Удаление сотрудника
            :param id(int): id сотрудника
            
            :return: None 
        """
        
        sql = text('''
            delete from employee
            where id = :id
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {'id': id})
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.commit()
            conn.close()
    
    @allure.step('bd. Создать сотрудника с передачей основных данных {body}')  
    def create_with_required(self,  body: dict) -> None:
        """
            Создание сотрудника с передачей обязательных параметров
            :param body(dict): параметры сотрудника в формате словаря
            
            :return: None 
        """
      
        sql = text('''
            insert into employee("first_name", "last_name", "phone", "company_id")
            values (:first_name, :last_name, :phone, :company_id)
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {
                'first_name': body['first_name'],
                'last_name': body['last_name'], 
                'phone': body['phone'],
                'company_id': body['company_id']
            })
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.commit()
            conn.close()
    
    @allure.step('bd. Создать сотрудника с передачей всех данных {body}')
    def create_with_all(self,  body: dict) -> None:
        """
            Создание сотрудника с передачей всех параметров
            :param body(dict): параметры сотрудника в формате словаря
            
            :return: None 
        """
      
        sql = text('''
            insert into employee("first_name", "last_name", "middle_name", "phone", "email", "avatar_url", "birthdate", "company_id")
            values (:first_name, :last_name, :middle_name, :phone, :email, :avatar_url, :birthdate, :company_id)
        ''')
        with self.__db.connect() as conn:
            query = conn.execute(sql, {
                'first_name': body['first_name'],
                'last_name': body['last_name'], 
                'middle_name': body['middle_name'],
                'phone': body['phone'],
                'email': body['email'],
                'avatar_url': body['avatar_url'],
                'birthdate': body['birthdate'],
                'company_id': body['company_id']
            })
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
            conn.commit()
            conn.close()
    
    @allure.step('bd. Получить max id сотрудника')    
    def get_max_id(self) -> int:
        """
            Получение максимального id сотрудника в БД
            
            :return: int: id сотрудника
        """
      
        sql = text('select MAX(id) as id from employee')
        with self.__db.connect() as conn:
            query = conn.execute(sql)
            result =  query.mappings().all()[0]['id']
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return result
