dict = { 'cat': 'pisica', 'dog': 'caine' }

try: 
  x = dict['mouse']
except KeyError: # or Exception - more generic
  print('Not found in dictionary')
finally:
  print('dictionary: ')
  for k,v in dict.items():
    print(k, v, sep=': ')

# raise custom error example
if 'mouse' not in dict.keys():
    raise Exception('word is not in dictionary')  