dictionary = {
  'LOL': 'laugh out loud',
  'IDK': 'I don\'t know',
  'TBH': 'to be honest'
}
del dictionary['LOL']
for k,v in dictionary.items():
  print(k, v, sep=' = ')

# print(dictionary['x']) # crashes with KeyError
print(dictionary.get('x'))
