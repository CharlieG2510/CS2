import sys
import random


board = [
["", "", ""],
["", "", ""],
["", "", ""],
         ]

def ai(board):
    #Checking if it can win this move
    if board[0][0] == 'o' and board[0][1] == 'o':
        if board[0][2] == '':
            board[0][2] = 'o'
    elif board[1][0] == 'o' and board[1][1] == 'o':
        if board[1][2] == '':
            board[1][2] = 'o'
    elif board[2][0] == 'o' and board[2][1] == 'o':
        if board[2][2] == '':
            board[2][2] = 'o'
    

    if board[0][0] == 'o' and board[0][2] == 'o':
        if board[0][1] == '':
            board[0][1] = 'o'
    elif board[1][0] == 'o' and board[1][2] == 'o':
        if board[1][1] == '':
            board[1][1] = 'o'
    elif board[2][0] == 'o' and board[2][2] == 'o':
        if board[2][1] == '':
            board[2][1] = 'o'
    

    if board[0][2] == 'o' and board[0][1] == 'o':
        if board[0][0] == '':
            board[0][0] = 'o'
    elif board[1][2] == 'o' and board[1][1] == 'o':
        if board[1][0] == '':
            board[1][0] = 'o'
    elif board[2][2] == 'o' and board[2][1] == 'o':
        if board[2][0] == '':
            board[2][0] = 'o'
    


    

    elif board[0][0] == 'o' and board[1][0] == 'o':
        if board[2][0] == '':
            board[2][0] = 'o'
    elif board[0][1] == 'o' and board[1][1] == 'o':
        if board[2][1] == '':
            board[2][1] = 'o'
    elif board[0][2] == 'o' and board[1][2] == 'o':
        if board[2][2] == '':
            board[2][2] = 'o'
    

    elif board[0][0] == 'o' and board[2][0] == 'o':
        if board[1][0] == '':
            board[1][0] = 'o'
    elif board[0][1] == 'o' and board[2][1] == 'o':
        if board[1][1] == '':
            board[1][1] = 'o'
    elif board[0][2] == 'o' and board[2][2] == 'o':
        if board[1][2] == '':
            board[1][2] = 'o'
    
    elif board[1][0] == 'o' and board[2][0] == 'o':
        if board[0][0] == '':
            board[0][0] = 'o'
    elif board[1][1] == 'o' and board[2][1] == 'o':
        if board[0][1] == '':
            board[0][1] = 'o'
    elif board[1][2] == 'o' and board[2][2] == 'o':
        if board[0][2] == '':
            board[0][2] = 'o'
    
    
    
    elif board[2][0] == 'o' and board[1][1] == 'o':
        if board[0][2] == '':
            board[0][2] = 'o'
    elif board[0][0] == 'o' and board[1][1] == 'o':
        if board[2][2] == '':
            board[2][2] = 'o'
    

    elif board[0][2] == 'o' and board[1][1] == 'o':
        if board[2][0] == '':
            board[2][0] = 'o'
    elif board[2][2] == 'o' and board[1][1] == 'o':
        if board[0][0] == '':
            board[0][0] = 'o'
    

    elif board[0][2] == 'o' and board[2][0] == 'o':
        if board[1][1] == '':
            board[1][1] = 'o'
    elif board[2][2] == 'o' and board[0][0] == 'o':
        if board[1][1] == '':
            board[1][1] = 'o'
    


    

    #Block other player
    elif board[0][0] == 'x' and board[0][1] == 'x':
        if board[0][2] == '':
            board[0][2] = 'o'
    elif board[1][0] == 'x' and board[1][1] == 'x':
        if board[1][2] == '':
            board[1][2] = 'o'
    elif board[2][0] == 'x' and board[2][1] == 'x':
        if board[2][2] == '':
            board[2][2] = 'o'
    

    elif board[0][0] == 'x' and board[1][0] == 'x':
        if board[2][0] == '':
            board[2][0] = 'o'
    elif board[0][1] == 'x' and board[1][1] == 'x':
        if board[2][1] == '':
            board[2][1] = 'o'
    elif board[0][2] == 'x' and board[1][2] == 'x':
        if board[2][2] == '':
            board[2][2] = 'o'

    
    elif board[2][0] == 'x' and board[1][1] == 'x':
        if board[0][2] == '':
            board[0][2] = 'o'
    elif board[0][0] == 'x' and board[1][1] == 'x':
        if board[2][2] == '':
            board[2][2] = 'o'
    
    #go to middle if open
    elif board[1][1] == '':
        board[1][1] == 'o'

    
    
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
    else:
        print('already smthn there >:(')
        



print(f"""

{board[0]}
{board[1]}
{board[2]}

""")




def has_won(board):
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        sys.exit()
    
    if board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        print('o has won yipee')
        sys.exit()
    
    if board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        sys.exit()
    
    

    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
        print('x has won yipee')
        sys.exit()
    
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        print('x has won yipee')
        sys.exit()
    
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        print('x has won yipee')
        sys.exit()





    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('o has won yipee')
        sys.exit()
    

    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        print('x has won yipee')
        sys.exit()
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        print('o has won yipee')
        sys.exit()
    


def is_tie(board):
    if board[0][0] == '' or board[0][1] == '' or board[0][2] == '' or board[1][0] == '' or board[1][1] == '' or board[1][2] == '' or board[2][0] == '' or board[2][1] == '' or board[2][2] == '':
        return False
    else:
        print('its a tie :(')
        sys.exit()
    

    



def main():
    turn = 'x'
    while True:
        move(turn, board)
        ai(board)
        print(f"""
{board[0]}
{board[1]}
{board[2]}""")
        has_won(board)
        is_tie(board)
main()

