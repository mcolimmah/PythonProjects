# Write your code here :-)
name = 'Al'
age = 4000
print('This is the Result using the Regular method!!!!!')
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')

print('\n')

print('In ten years I will be ' + str(age + 10))

''' instead, use f-strings, it is simpler '''
print('This is the Result using the f-string method!!!!!')
name = 'Al'
age = 4000

print('''
''')
print(f'My name is {name}. I am {age} years old.')
print('\n')
print(f'In ten years, my name will still be {name}, and I will be {age + 10}')

''' F-String Alternatives, The %s and format() '''
print('\n')
print('This is the Result using the %s method!!!!!')
print('My name is %s. I am %s years old.' % (name, age+5))
print('In ten years I will be %s' % (age + 10))

''' Format Method'''
print('\n')
print('This is the Result using the format method, \n this method is typically better when you are inserting values out of order !!!')
print('My name is {}. I am {} years old. ' .format(name, age))

name = 'Al'
age = 4000
print('\n')
print('{1} years ago, {0} was born and named {0}.'.format(name, age))

height =18
age = 40
name = 'Marsh'
print('The age of {2} is very close to {1}, and his height is very close to {0}, ' .format(height, age, name))
