# Write your code here :-)
import random

while True:

    messages = [' It is certain ', ' It is decidedly so ', ' Yes Definitely ',
    ' Reply Hazy Try Again ', ' Ask Again Later ', ' Concentrate and Ask Again ',
    ' My Reply is No ', ' Outlook not so Good ', ' Very Doubful ']

    print('Ask a yes or no Question: ')
    input('>>>>>>>>')
    #print(messages[random.randint(0, len(messages)-1)])
    print([random.choice(messages)])

    continue



