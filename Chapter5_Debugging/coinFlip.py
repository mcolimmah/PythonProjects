# Write your code here :-)
import random

heads = 0
tails = 0

for i in range(1, 1001):

    if i == 500:
        print('Halfway done!')

    if random.randint(0, 1) == 1:
        heads = heads + 1
    else:
        tails = tails + 1



print('Heads came up ' + str(heads) + ' times.' + " And Tails Came up " + str(tails) + ' times ')
