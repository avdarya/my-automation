import pytest

empty_dict = {}

football_stats = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": ["Австралия", "Англия", "Аргентина", "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {
        "Золотой мяч": "Лионель Месси",
        "Серебряный мяч": "Килиан Мбаппе",
        "Золотая бутса": "Килиан Мбаппе",
        "Серебряная бутса": "Килиан Мбаппе",
        "Больше всего голов": {
            "Игрок": "Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        }
    }
}

def test_empty_dict():
  assert len(empty_dict) == 0
  
def test_read_value_by_get():
  count = football_stats.get('Число стран')
  assert count == 48
  
def test_read_value_by_key():
  assert football_stats['Страна'] == 'Катар'
  
def test_update_value():
  football_stats["Число стран"] = 50
  country = football_stats.get('Число стран')
  assert country == 50
  
def test_write_new_value():
  len_before = len(football_stats)
  football_stats['Победитель'] = 'Аргентина'
  country = football_stats['Победитель']
  assert country == 'Аргентина'
  assert len(football_stats) == len_before + 1
  
def test_read_list():
  engLand = football_stats['Участники'][1]
  assert engLand == 'Англия'
  
def test_read_dict():
   goals = football_stats['Награды ']['Больше всего голов']['Количество мячей']
   assert goals == 8
   
def test_read_error_by_key():
  with pytest.raises(KeyError):
    empty_dict['key']
    
def test_read_error_by_get():
  value = empty_dict.get('key', '000')
  assert value == '000'