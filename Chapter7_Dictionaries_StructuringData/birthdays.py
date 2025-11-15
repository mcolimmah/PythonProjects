# Write your code here :-)
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (enter exit to quit)')
    name = input('>>>>>>>>>>')
    if name == 'exit':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have birthday information for ' + name)
        print('What is their Birthday?')
        bday = input('>>>>>>>>>>>')
        birthdays[name] = bday
        print('Birthday database updated. ')

