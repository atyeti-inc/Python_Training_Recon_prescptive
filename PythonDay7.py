file=r'C:\Users\HemantGandhi\OneDrive - Atyeti Inc\Desktop\PythonDay7.txt'
with open(file, 'w') as FILE:
    FILE.write('Hello!\nPython File handling practice')

with open(file, 'r') as FILE:
    Content=FILE.read()
    print(Content)

with open(file, 'a') as FILE:
    FILE.write('\nTrue, This is an appended line')

with open(file, 'r') as FILE:
    print('______________________To read the lines from a file_______________')
    content=FILE.readlines()
    print(content)
    print('The count of lines in file is',len(content))

with open(file, 'r') as FILE:
    contents=FILE.readlines()
    for i in contents:  
      if 'True' in i:
        print(i)

import os
if os.path.isfile(file):
   print('The file',file, 'exists...')
else:
   print('The file',file, 'does not exists...')