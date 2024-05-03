class Calculator:

  def sum(self, a, b):
    return a + b
  
  def sub(self, a, b):
    return a - b
  
  def mul(self, a, b):
    return a * b
  
  def div(self, a, b):
    if b == 0:
      raise ArithmeticError('На ноль делить нельзя')
    else:
      return a / b
  
  def pow(self, a, b):
    return a ** b
  
  def avg(self, nums):
    if len(nums) == 0:
      return 0
    
    s = 0
    for num in nums:
      s = self.sum(s, num)

    return self.div(s, len(nums))