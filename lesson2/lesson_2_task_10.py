def bank(initial_summ, year):
  return initial_summ * pow((1 + 10 / 100), year)
    
print(bank(20000, 5))