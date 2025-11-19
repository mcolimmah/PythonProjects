# Write your code here :-)
bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
bacon_file.write('Hello, world!\n')

bacon_file.close()
bacon_file = open('bacon.txt', 'a', encoding='UTF-8')
bacon_file.write('Bacon is not a vegetable.')

bacon_file.close()

bacon_file= open('bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()


bacon_file= open('bacon.txt', 'a', encoding='UTF-8')
bacon_file.write("When,in disgrace with fortune and men's eyes,\n"
"I all alone beweep my outcast state,\n"
"And trouble deaf heaven with my bootless cries,\n"
"And look upon myself and curse my fate")

bacon_file.close()

bacon_file= open('bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()
print(content)

## Equivalent statement using the with statement, no need to close the file
'''
with open('data.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('Hello, world!')
with open('data.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()

