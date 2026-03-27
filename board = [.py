import sys
import pygame
import random


''''
Name: Charlie Gordon
Description: Play Tic Tac Toe against an AI
Date: 4/1/25
Bugs: N/A
Sources: Mr. Campbell
Log: 1.0
'''




def music(sound):
    '''
    Desc: Plays a sound effect when called upon
    Args: Sound(str)
    Returns: Sound effect
    '''
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(9)
    pygame.quit()



def move(turn, board, x, o):
    '''
    Desc: Allows the player to place their move on the board
    Args: Board(list), Turn(str)
    Returns: X or O on a part of board
    
    '''
    while True:
        while True:
            if turn == 'x':
                row = input(f'{x}, you are x, what row do you want(type 1, 2 or 3)')
            else:
               row = input(f'{o}, you are o, what row do you want(type 1, 2 or 3)')
            if row == '1' or row == '2' or row == '3':
                pass
            else:
                print('impossible')
                continue
            column = input(f'what column do you want (type 1, 2 or 3)')
            if column == '1' or column == '2' or column == '3':
                break
            else:
                print('impossible')
                continue
        if board[int(row)-1][int(column)-1] == '':
            board[int(row)-1][int(column)-1] = turn
            break
        else:
            print('already something there')
        








def has_won(board):
    '''
    Desc: Checks if X or O have 3 in a row in every possible combination
    Args: Board(list)
    Returns: N/A (ends program if they have won after playing a sound effect and printing who won)
    
    '''
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    
    if board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    
    if board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    
    

    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False





    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False
    

    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        return False
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        music('Celebration.mp3')
        return False


def is_tie(board):
    '''
    Desc:Checks if any spaces are left and if they are not, then say its a tie
    Args: Board(list)
    Returns: O on a part of board
    
    '''
    if board[0][0] == '' or board[0][1] == '' or board[0][2] == '' or board[1][0] == '' or board[1][1] == '' or board[1][2] == '' or board[2][0] == '' or board[2][1] == '' or board[2][2] == '':
        return False
    else:
        print('its a tie :(')
        print(f"""
{board[0]}
{board[1]}
{board[2]}""")
        music('failure.mp3')
        return True
    




def main():
    #Actual board that will be used to keep track for
    board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
            ]
    
    player1 = input('player 1 type name')
    player2 = input('player 2 type name')
    names = [player1, player2]
    #Makes random player x
    x = random.choice(names)

    names.remove(x)
    #Makes other player o
    o = random.choice(names)

    turn = 'x'
    print(f"""

{board[0]}
{board[1]}
{board[2]}

""")
    while True:
        #Have the first player move
        move(turn, board, x, o)
        #change the turn
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'
        #show what he did
        print(f"""
{board[0]}
{board[1]}
{board[2]}""")
        #check for winners or a tie
        if has_won(board) == False:
            board = [
["", "", ""],
["", "", ""],
["", "", ""],
         ]
            continue
        if is_tie(board) == True:
            board = [
["", "", ""],
["", "", ""],
["", "", ""],
         ]
            continue
main()

