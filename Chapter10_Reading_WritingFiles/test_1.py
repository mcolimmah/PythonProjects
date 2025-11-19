# Write your code here :-)

'''
from pathlib import Path
Path('spam', 'bacon', 'egg')   ### I can just assign this to a variable and just call the variable instead.
c = Path('spam', 'bacon', 'egg')
d = str(c)

'''




from pathlib import Path
my_files = ['accounts.txt', 'details.csv', 'invite.docx']

for i in my_files:                      ### For filename in my_files
    print(Path(r'C:\Users\Al', i))      ### print(Path(r'C:\Users\Al', Filename))



'''
c = print('Hello'+'World')

from pathlib import Path
import os

path_1 = Path.cwd()    ### To get the current working directory and put the result in variable pathh
path_2 = os.getcwd()   ## Older method of doing line 28
#path_3 = os.chdir('')  ### To change directory to the address specified in the path_2 variable
path_4 = Path.home()

import os
folder_1 = os.makedirs('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles/folder_2')
## The above line creates a new folder named folder_1 in the absolute path
## it would also create all the necessary intermediate folders required to work the address specified
folder_2 = Path(r'C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles/folder_1').mkdir()
'''

from pathlib import Path
p = Path('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles/folder_1/spam.txt')
## Run any of the following for details of the file path and file
## p.anchor, p.parent , p.name , p.stem, p.suffix, p.drive, p.parts

## Using Glob(*) to locate files matching
from pathlib import Path
k = Path('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter8_Strings_TextEditing')
k.glob('*')

## list(k.glob('*'))
## or just use a for loop
from pathlib import Path
for name in Path('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter8_Strings_TextEditing').glob('*'):
    print(name)

## check if exsits  name.is_dir(), name.is_file(), name.exists()

from pathlib import Path
d_drive = Path('D:/')
d_drive.exists()
