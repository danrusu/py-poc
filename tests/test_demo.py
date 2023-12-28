class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  

import pytest

a = 1

@pytest.fixture
def person1():
  "Provides a test Person - Dan:42"
  return Person('Dan', 42)  

@pytest.fixture
def person2():
  "Provides a test Person - dorina:40"
  return Person('Dorina', 40)  


@pytest.mark.skip("WIP")
def test_demo():
  assert 1 == 2

@pytest.mark.slow
def test_slow():
  assert 1 == 2

def test_error_is_raised():
  with pytest.raises(KeyError):
    #x = {'one':1, 'two': 2}['one']    
    x = {'one':1, 'two': 2}['three']    

def test_fixture(person1, person2):
  assert person1.name == 'Dan'
  assert person2.age == 40

@pytest.mark.parametrize(
    "name,age,is_over_40", [
      ('Dan', 42, True), 
      ('Dorina', 40, True)
    ]    
)
def test_parameterized(name, age, is_over_40):
  print(f'{name}(age: {age}) is over 40: {is_over_40}')    
  #assert age > 45  