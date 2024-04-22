def is_year_leap(year):
  return year % 4 == 0

checking_year = 2021
result = is_year_leap(checking_year)
print('год ',checking_year,': ',result)