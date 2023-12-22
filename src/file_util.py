import os
import shutil #file utilities

newFolder = os.path.join('src', '..', 'new_folder')
newFile1 = os.path.join(newFolder, 'newFile1.txt')
newFile2 = os.path.join(newFolder, 'newFile2.txt')

def cleanup():
  try:
    os.remove(newFile2)    
    os.rmdir(newFolder)
  except Exception:
    print('cleanup not needed')

def list_folder_entries(folder):  
  for entry in os.scandir(folder):
    print(entry.name)

# main

cleanup()

os.mkdir(newFolder)
with open(newFile1, 'w') as file:
  file.write('demo')

list_folder_entries(newFolder)

os.rename(newFile1, newFile2)
list_folder_entries(newFolder)

print(os.path.expanduser(
  os.path.join('~','Desktop'))
)
