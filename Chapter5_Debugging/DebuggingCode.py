# Write your code here :-)
import random
heads = 0
tails = 0

guess = ' '
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 1:
    ('print, toss is heads')
    heads = heads + 1
else:
   tails = tails + 1

if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guess = input()

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
