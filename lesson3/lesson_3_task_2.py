from smartphone import Smartphone

catalog = [ 
  Smartphone('brand_1', 'model_1', '+7 911 111 11 11'),
  Smartphone('brand_2', 'model_2', '+7 922 222 22 22'),
  Smartphone('brand_3', 'model_3', '+7 933 333 33 33'),
  Smartphone('brand_4', 'model_4', '+7 944 444 44 44'),
  Smartphone('brand_5', 'model_5', '+7 955 555 55 55'),
]

for item in catalog:
  print(f'{item.brand} - {item.model}. {item.number}')