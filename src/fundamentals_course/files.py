#file = open('src/../resource/acronyms.txt')

# auto close
with open('src/../resource/acronyms.txt', 'r', encoding='utf-8') as file:
  # lines = file.readlines()
  # print(lines)
  for line in file:
    print(line)


with open('src/../resource/acronyms.txt', 'a', encoding='utf-8') as file:
  file.writelines(['\nline1', '\nline2'])
  for line in ['\nTBH: to be honest', '\nlast']:
    file.write(line)