import random #SDK

choice = random.choice(['paper', 'scisors', 'rock'])
print('Random choice: ' + choice)

acronyms = ['LOL', 'IDK', 'SMH']
acronyms.append('TBH')
print(acronyms)

del acronyms[0]
for acronym in acronyms:
  print(acronym)

word = 'LOL'
if 'LOL' in acronyms:
  print(word, 'found in', str(acronyms))

print('this-', 'that', sep='')

for i in range(0, 10, 2):
  print(i)
