import random

#global variables
GRID = 5
USER_BOARD = [[' '] * GRID for i in range(GRID)]
COMP_BOARD = [[' '] * GRID for i in range(GRID)]
USER_GUESS_BOARD = []
COMP_GUESS_BOARD = []
TRANSLATE_LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    '''print board function'''
    print(' A B C D E F G H ')
    print(' =================')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1
    print(' =================')
print_board(COMP_BOARD)

def place_ships(board):
    '''place ships on the board'''
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)
    board[ship_row][ship_col] = 'O'

def user_input():
    '''get user input'''
    pass


def ships_hit():
    '''count ships hit'''
    pass




