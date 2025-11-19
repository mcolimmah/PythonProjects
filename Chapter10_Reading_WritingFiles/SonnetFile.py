# Read the sonnet File i Created in notepadWrite your code here :-)
from pathlib import Path
#sonnet_file = open('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles/sonnet29.txt', encoding= 'UTF-8')
sonnet_file = open('sonnet29.txt', encoding= 'UTF-8')
sonnet_file.readlines()

from pathlib import Path
p = Path('sonnet29a.txt')

#p.write_text('My name is Marshal and I am the best')

k = Path('sonnet29b.txt')
k.write_text("When,in disgrace with fortune and men's eyes,\n"
"I all alone beweep my outcast state,\n"
"And trouble deaf heaven with my bootless cries,\n"
"And look upon myself and curse my fate")

sonnet_file = open('C:/Users/mcolimmah/OneDrive/PYTHON Programming/PythonProjects/Chapter10_Reading_WritingFiles/sonnet29b.txt', encoding= 'UTF-8')
sonnet_file.readlines()



