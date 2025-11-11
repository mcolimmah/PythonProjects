# ## My own designed Game of the ROCK PAPER SCISSORS GAME between A player and computer Write your code here :-)

## Declare the number of variables

wins = 0
losses = 0
ties = 0

### import the Required modules to run it 
import sys

while True:   ## The main loop Game
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  ## The Player input loop
        print('Enter Your Move: (r) for ROCK, (p) for PAPER, (s) for SCISSORS, or (q) for QUIT')
        player_move = input('>>>>>>>>>>')
        if player_move == 'q':
            print ('The user quit the program without Reason!!!!!!')
            sys.exit()    ### Quit the Program
            
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')
            
        ### Now let us generate the computer selection
        ### I can assign move numbers from 1 to 3 for the selections (1) For Rock (2) For Paper (3) For Scissors
        import random
        move_number = random.randint(1,3)
        
        if move_number == 1:
            computer_move = 'r'
        elif move_number == 2:
            computer_move = 'p'
        elif move_number == 3:
            computer_move = 's'
            
        #### Try
        if player_move == computer_move:
            print('It is a super tie!!')
            ties = ties + 1
        elif player_move == 'r' and computer_move == 's':
            print('You win this Round')
            wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
            print('You also win this Round')
            wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
            print('Another Win for you')
            wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
            print('A Loss for you')
            losses = losses + 1
        elif player_move == 's' and computer_move == 'r':
            print('Another loss for you')
            losses = losses + 1
        elif player_move == 'p' and computer_move == 's':
            print('Another loss for you')
            losses = losses + 1  
        
        
        
       # if player_move == 'r' and computer_move == 'r':
            #print ('Player chose Rock and Computer Chose Rock')
       # elif player_move == 'p' and computer_move == 'p':
           # print ('Player chose PAPER and Computer Chose PAPER')
        #elif player_move == 's' and computer_move == 's':
            #print ('Player chose SCISSORS and Computer Chose SCISSORS')
       # elif player_move == 'r' and computer_move == 's':
            #print ('Player chose ROCK and Computer Chose SCISSORS')
       # elif player_move == 'p' and computer_move == 'r':
            #print ('Player chose PAPER and Computer Chose ROCK')
       # elif player_move == 's' and computer_move == 'p':
            #print ('Player chose SCISSORS and Computer Chose PAPER')
       # elif player_move == 'r' and computer_move == 'p':
            #print ('Player chose ROCK and Computer Chose PAPER')
       # elif player_move == 'p' and computer_move == 's':
            #print ('Player chose PAPER and Computer Chose SCISSORS')