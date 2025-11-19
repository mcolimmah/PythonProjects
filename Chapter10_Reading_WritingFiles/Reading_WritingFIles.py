# Write your code here :-)
## Create a text file automatically with the current working directory

from pathlib import Path
p = Path('Hello.txt')
p.write_text('Hello, World!')   ### This line actually creates the file if it doesnt exists

c= p.read_text()     ## This line reads the contents contained in the file


'''
Marsh = ['Hello, World!', 'Helicopters are Amazing', ' I want to be wealthy']


Q = Path('Marshal.txt')
for contents in Marsh:
    Q.write_text(contents[0:len(contents)])

'''

filepath = 'C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles'

'''
from pathlib import Path
hello_file = filepath.write_text('hello.txt')
'''
from pathlib import Path
hello_file = open('Hello.txt', encoding= 'UTF-8')

hello_content = hello_file.read()
hello_content
