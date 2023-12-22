class Person:
  count = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def print(self):
    print(f'name: {self.name}, age: {self.age}')

  def message(self):    
    print('I am a Person')

  @staticmethod
  def static_method():  
    return "I am a static method"

  @classmethod
  def counter(cls):  
    cls.count += 1
    

class Employee(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.employed = True

  # override
  def message(self):
    print('I am an Employee')

  def _dispaly(self):  # Private
    print("Hello")