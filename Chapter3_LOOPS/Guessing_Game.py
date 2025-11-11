# Let us create a Guessing Game:-)

import random

secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')


## Ask the Player to guess 6 times.

for guesses_taken in range(1,6):
    print('Take a Guess. ')
    guess = int(input('>>>'))


    if guess < secret_number:
        print('Your Guess is too low.')
    elif guess > secret_number:
        print ('Your Guess is too high.')
    #elif guess == secret_number:
        #print ('Your guess is correct and wonderful, Good Job')

        #break

    else:
        break ## This condition is the correct Guess!


if guess == secret_number:
    print('Good Job! You got it in ' + str(guesses_taken) + 'Guesses!')

else:
    print('Nope. The number was ' + str(secret_number))
