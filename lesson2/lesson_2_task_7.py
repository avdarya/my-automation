from functools import reduce

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# 1 вариант
print(reduce(lambda a, b: a + b, lst, 0))

# 2 вариант
sum = 0
for i in range(0, len(lst)):
  sum += lst[i]
print(sum)