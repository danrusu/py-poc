from classes import Person, Employee

person = Person('Dan', 42)
person.print()
person.message()
print(person.name, 'is', person.age, 'years old')

print(Person.static_method())

Person.counter()
Person.counter()
print(f'Person count: {Person.count}')

print('--------------------------------')

employee = Employee('Dorina', 41)
employee.print()
print(employee.employed)
employee.message()