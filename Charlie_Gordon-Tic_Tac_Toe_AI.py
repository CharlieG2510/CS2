import sys
import random
import pygame

board = [
["", "", ""],
["", "", ""],
["", "", ""],
         ]


def music(sound):
    #Desc: Plays a sound effect when called upon
    #Args: Sound(str)
    #Returns: Sound effect
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(9)
    pygame.quit()



def ai(board):
    '''
    Desc:The AI blocks any potential winning moves for the player, checks if it can win and does that if it can, checks if the middle is open, and if none of that happens it does a random move
    Args: Board(list)
    Returns: O on a part of board
    
    '''
    #Checking if it can win this move
    if board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == '':
            board[0][2] = 'o'
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == '':
        
            board[1][2] = 'o'
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == '':
        
            board[2][2] = 'o'
    

    if board[0][0] == 'o' and board[0][2] == 'o':
        if board[0][1] == '':
            board[0][1] = 'o'
    elif board[1][0] == 'o' and board[1][2] == 'o' and board[1][1] == '':
        
            board[1][1] = 'o'
    elif board[2][0] == 'o' and board[2][2] == 'o' and board[2][1] == '':
        
            board[2][1] = 'o'
    

    if board[0][2] == 'o' and board[0][1] == 'o' and board[0][0] == '':
        
            board[0][0] = 'o'
    elif board[1][2] == 'o' and board[1][1] == 'o' and board[1][0] == '':
        
            board[1][0] = 'o'
    elif board[2][2] == 'o' and board[2][1] == 'o' and board[2][0] == '':
        
            board[2][0] = 'o'
    


    

    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == '':
        
            board[2][0] = 'o'
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == '':
        
            board[2][1] = 'o'
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == '':
        
            board[2][2] = 'o'
    

    elif board[0][0] == 'o' and board[2][0] == 'o' and board[1][0] == '':
        
            board[1][0] = 'o'
    elif board[0][1] == 'o' and board[2][1] == 'o' and board[1][1] == '':
        
            board[1][1] = 'o'
    elif board[0][2] == 'o' and board[2][2] == 'o' and board[1][2] == '':
        
            board[1][2] = 'o'
    
    elif board[1][0] == 'o' and board[2][0] == 'o' and board[0][0] == '':
        
            board[0][0] = 'o'
    elif board[1][1] == 'o' and board[2][1] == 'o' and board[0][1] == '':
    
        board[0][1] = 'o'
    elif board[1][2] == 'o' and board[2][2] == 'o' and board[0][2] == '':
    
        board[0][2] = 'o'
    
    
    
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == '':
        
            board[0][2] = 'o'
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == '':
        
            board[2][2] = 'o'
    

    elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == '':
    
        board[2][0] = 'o'
    elif board[2][2] == 'o' and board[1][1] == 'o' and board[0][0] == '':
    
        board[0][0] = 'o'
    

    elif board[0][2] == 'o' and board[2][0] == 'o':
        if board[1][1] == '':
            board[1][1] = 'o'
    elif board[2][2] == 'o' and board[0][0] == 'o' and board[1][1] == '':
    
        board[1][1] = 'o'
    


    

    #Block other player
    elif board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == '':
        
            board[0][2] = 'o'
    elif board[0][2] == 'x' and board[0][1] == 'x' and board[0][0] == '':
        board[0][0] = 'o'
    elif board[0][2] == 'x' and board[0][0] == 'x' and board[0][1] == '':
        
            board[0][1] = 'o'
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == '':
        board[1][2] = 'o'
    elif board[1][2] == 'x' and board[1][1] == 'x' and board[1][0] == '':
        board[1][0] = 'o'
    elif board[1][0] == 'x' and board[1][2] == 'x' and board[1][1] == '':
        board[1][1] = 'o'
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == '':
        board[2][2] = 'o'
    elif board[2][2] == 'x' and board[2][1] == 'x' and board[2][0] == '':
        board[2][0] = 'o'
    elif board[2][0] == 'x' and board[2][2] == 'x' and board[2][1] == '':
        board[2][1] = 'o'
    

    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == '':
        board[2][0] = 'o'
    elif board[2][0] == 'x' and board[1][0] == 'x' and board[0][0] == '':
        board[0][0] = 'o'
    elif board[0][0] == 'x' and board[2][0] == 'x' and board[1][0] == '':
        board[1][0] = 'o'
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == '':
        board[2][1] = 'o'
    elif board[2][1] == 'x' and board[1][1] == 'x' and board[0][1] == '':
        board[0][1] = 'o'
    elif board[2][1] == 'x' and board[1][1] == 'x' and board[0][1] == '':
        board[0][1] = 'o'
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == '':
        board[2][2] = 'o'
    elif board[2][2] == 'x' and board[1][2] == 'x' and board[0][2] == '':
        board[0][2] = 'o'
    elif board[0][2] == 'x' and board[2][2] == 'x' and board[1][2] == '':
        board[1][2] = 'o'

    
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == '':
        board[0][2] = 'o'
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == '':
        board[2][0] = 'o'
    elif board[2][0] == 'x' and board[0][2] == 'x' and board[1][1] == '':
        board[1][1] = 'o'
    elif board[0][0] == 'x' and board[1][1] == 'x' and  board[2][2] == '':
        board[2][2] = 'o'
    elif board[2][2] == 'x' and board[1][1] == 'x' and board[0][0] == '':
        board[0][0] = 'o'
    elif board[0][0] == 'x' and board[2][2] == 'x' and board[1][1] == '':
        board[1][1] = 'o'
            
    
    #check if middle is avaliable
    elif board[1][1] == '':
        board[1][1] = 'o'
    
    #else do a random move
    else:
        while True:
            random_column = random.randint(0,2)
            random_row = random.randint(0,2)
            if board[random_row][random_column] == '':
                board[random_row][random_column] = 'o'
                break
            else:
                continue
    


    
    





def move(turn, board):
    '''
    Desc: Allows the player to place their move on the board
    Args: Board(list), Turn(str)
    Returns: X or O on a part of board
    
    '''
    while True:
        while True:
            column = input(f'{turn} what column do you want (type 1, 2 or 3)')
            if column == '1' or column == '2' or column == '3':
                pass
            else:
                print('impossible')
                continue
            row = input('what row do you want(type 1, 2 or 3)')
            if row == '1' or row == '2' or row == '3':
                break
            else:
                print('impossible')
                continue
        if board[int(row)-1][int(column)-1] == '':
            board[int(row)-1][int(column)-1] = turn
            break
        else:
            print('already smthn there >:(')
        



print(f"""

{board[0]}
{board[1]}
{board[2]}

""")




def has_won(board):
    '''
    Desc: Checks if X or O have 3 in a row in every possible combination
    Args: Board(list)
    Returns: N/A (ends program if they have won after playing a sound effect and printing who won)
    
    '''
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
    
    if board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
    
    if board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
    
    

    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
        
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
        
    
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
        
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
        
    
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
        
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
        





    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
        
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
        
    

    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        music('Celebration.mp3')
        sys.exit()
        
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        music('failure.mp3')
        sys.exit()
    

    


        
    


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
    turn = 'x'
    while True:
        move(turn, board)
        #Prints the board in a way where each list is in 3 in a row
        print(f"""
{board[0]}
{board[1]}
{board[2]}""")
        has_won(board)
        #if its a tie
        if is_tie(board) == True:
            break
        ai(board)
        print(f"""
{board[0]}
{board[1]}
{board[2]}""")
        has_won(board)
        if is_tie(board) == True:
            break
main()

