## Magic 8 Ball Code
# Write your code here :-)

import random

def get_answer(answer_number):
    #Return a fortune answer based on what int answer_number is, 1 to 9
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return ' Ask Again Later'
    elif answer_number == 6:
        return 'Concentrate and Ask Again'
    elif answer_number ==7:
        return 'My Reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very Doubtful'

print('Ask a yes or no Question: ')
input('>>>>>>>>>')
r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)

## print(get_answer(random.randint(1,9)))
