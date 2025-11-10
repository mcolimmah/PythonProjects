## The elif statement # Write your code here :-)

name = 'James' #input('Enter the Required name here >>>>>>')
age  = 15 #input('Enter the Required Age here >>>>>> ')

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print ('You are not Alice, Kiddo.')
elif name == 'Alice' and age != 12:
    print ('You might be Alice but not the right Age')
elif name != "Alice" and age == 12:
    print('You might be the right age, but definitely not Alice')

else:
    print('You are neither Alice nor are you the right age')
print('This is the input you gave the Username as ' + str(name) + ' and Age as ' + str(int(age)))  ## I put this code here to cover the entire code.

