# Write your code here :-)
Welcome_message = ' Welcome to my Python Program, Written by Marshal Olimmah '
Welcome_message = Welcome_message.center(100, '*')
print(Welcome_message)

t_1 = 'Hello'.rjust(10)
t_2 = 'Hello'.rjust(20)
t_3 = 'Hello, World'.rjust(20)
t_4 = 'Hello'.ljust(10)

vart = 'Hello'
t_5 = vart.rjust(len(vart)+1,'*')
t_6 = vart.rjust(len(vart)+2,'*')
t_7 = vart.rjust(len(vart)+3,'*')


print(t_5)
print(t_6)
print(t_7)
t_8 = 'Hello'.center(20)

t_9 = 'Hello'.center(20, '=')

''' Removing Whitespaces '''
spam = ' Hello, World '
spam.strip()
spam.lstrip()
spam.rstrip()

Goodbye_message = 'I hope you enjoyed using this software Program I wrote for you'
Goodbye_message = Goodbye_message.center(100, '=')
print(Goodbye_message)

