# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:00:07 2020

@author: UTKARSH SHANKAR
"""
# In[ ]:

from IPython.display import clear_output
import random

theBoard = [' '] * 10   
available = [str(num) for num in range(0,10)] 
players = [0,'X','O'] 

# In[]:
def display_board(a,b):
    print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n  '+
          '-----        -----\n  '+
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  '+
          '-----        -----\n  '+
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')
# In[]:
def player_input():
    marker=' '
    while marker !='X' and marker !='O':
        
        marker=input('Player1, choose X or O to play TIC-TAC_TOE :')
        player1=marker
        if player1=='X':
            
            player2='O'
        else:
             
            player2='X'
            
    return(player1,player2) 
# In[]:

def win_check(board, mark):
    
    return(board[7]==board[8]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or board[7]==board[5]==board[3]==mark or board[1]==board[5]==board[9]==mark or board[7]==board[4]==board[1]==mark or board[8]==board[5]==board[2]==mark or board[9]==board[6]==board[3]==mark)

# In[]:
 
def choice(board,player):
    position = 0
    
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Player %s, choose your next position: (1-9)'%(player) )
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('Enter a valid position!')        
    return int(position)
# In[]:
def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def random_player():
    return random.choice((-1, 1))
# In[]:
def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '   
    
# In[]:

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ')
# In[]:
while True:
    clear_output()
    print('Welcome to Tic_Tac-Toe!')
    
    toggle = random_player()
    player = players[toggle]
    print('For this round, Player %s will go first!' %(player)) 
    game_on = True
    input('Hit Enter to continue!')
    while game_on:
        display_board(available,theBoard)
        position = choice(theBoard,player)
        place_marker(available,theBoard,player,position)

        if win_check(theBoard, player):
            display_board(available,theBoard)
            print('Congratulations! Player '+player+' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available,theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                clear_output()

    # reset the board and available moves list
    theBoard = [' '] * 10
    available = [str(num) for num in range(0,10)]
    
    if not replay():
        print("\nThank You for Playing!\n\n   -Utkarsh")
        break



    