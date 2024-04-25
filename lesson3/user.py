class User:
  age = 0

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def printFirstName(self):
    print(self.first_name)

  def printLastName(self):
    print(self.last_name)

  def printFio(self):
    print(self.first_name, self.last_name)