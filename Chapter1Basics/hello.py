# This is a program that says hello and asks for my name. #
print()  ## This adds a blank line into the output for better readability
print('What is your name? ')  # Ask for their name.

print('Hello, World!')
print()  ## This adds a blank line into the output for better readability
my_name = input('Please tell me your name after this prompt >>>>>> ')
print('It is good to meet you, ' + my_name)
print('The length of your name is: ')
print(len(my_name))
print('What is your age? ') # Ask users for their age.
my_age = input('Please tell me your age after this prompt >>>>>>> ')
print()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
# print(f'You will be {int(my_age) +1} in a year')  # This format makes the result cleaner




