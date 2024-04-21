from math import ceil


def square(num):
  if isinstance(num, float):
    return ceil(num) * ceil(num)
  else:
    return num * num

sides = [5, 5.1]

for side in sides:
  print('площадь квадрата с стороной ', side, ' = ', square(side))