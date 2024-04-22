def bank(initial_summ, year):
  return initial_summ * pow((1 + 0.1), year)
    
print(bank(20000, 5))