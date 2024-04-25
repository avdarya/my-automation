from address import Address
from mailing import Mailing

from_address = Address('555 555', 'Novosibirsk', 'Ivanova', 10, 1)
to_address = Address('999 999', 'Moscow', 'Lenina', 4, 2)
mailing = Mailing(to_address, from_address, 1000, 'CLOD-58393')

print(f'Отправление {mailing.track} из '
      f'{mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, '
      f'{mailing.from_address.house} - {mailing.from_address.flat} '
      f'в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, '
      f'{mailing.to_address.house} - {mailing.to_address.flat}. ' 
      f'Стоимость {mailing.cost} рублей.'
)