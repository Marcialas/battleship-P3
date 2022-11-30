import random


# global variables

GRID = 8
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_GUESS_BOARD = [[' '] * 8 for i in range(8)]
COMP_GUESS_BOARD = [[' '] * 8 for i in range(8)]
TRANSLATE_LETTERS_TO_NUMBERS = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
    }


def print_board(board):
    '''print board function'''
    print('  A B C D E F G H ')
    print(' =================')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1
    print(' =================')


def place_ships(board):
    '''place ships on the board'''
    for ship in range(5):
        ship_row, ship_col = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_col] == 'O':
            ship_row, ship_col = random.randint(0, 7), random.randint(0, 7)
        board[ship_row][ship_col] = 'O'


def user_input():
    '''get users shot location input'''
    row = input('Please enter your shot row (1-8): ')
    while row not in '12345678':
        print('Please enter a valid row (1-8) ')
        row = input('Please enter your shot row (1-8): ')
    col = input('Please enter your shot column (A-H): ').upper()
    while col not in 'ABCDEFGH':
        print('Please enter a valid column (A-H')
        col = input('Please enter your shot column (A-H): ').upper()
    return int(row) - 1, TRANSLATE_LETTERS_TO_NUMBERS[col]


def ships_hit(board):
    '''count ships hit'''
    ships = 0
    for row in board:
        for col in row:
            if col == 'X':
                ships += 1
    return ships


def main():
    '''main game function'''
    print('=============================================')
    print('WELCOME TO THE CLASSIC GAME OF BATTLESHIPS!!!')
    print('=============================================')
    place_ships(USER_BOARD)
    place_ships(COMP_BOARD)
    while ships_hit(USER_GUESS_BOARD) or ships_hit(COMP_GUESS_BOARD) < 5:
        print_board(USER_BOARD)
        print_board(COMP_BOARD)
        print_board(USER_GUESS_BOARD)
        print_board(COMP_GUESS_BOARD)
        row, col = user_input()
        if COMP_BOARD[row][col] == 'O':
            print('You have hit an enemy ship!!!')
            USER_GUESS_BOARD[row][col] = 'X'
        elif USER_GUESS_BOARD[row][col] == ' ':
            print('You missed!!!')
            USER_GUESS_BOARD[row][col] = '#'
        elif USER_GUESS_BOARD[row][col] == '#':
            print('Shot already has been fired at this location')
        elif ships_hit(USER_GUESS_BOARD) == 5:
            print('Congrats!!! You Win!!!')
            break
        elif ships_hit(COMP_GUESS_BOARD) == 5:
            print('You Lose!!!')
            break
        print(ships_hit(USER_GUESS_BOARD))

    
        








if __name__ == '__main__':
    main()
