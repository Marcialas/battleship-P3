import random

# Game board LEGEND
# Marks that ship has been hit X
# Marks that shot has missed it's target #
# Marks a ship that has not been sunk yet O

# To Do list for future
# Ask user for game board size
# Code for the user to place own ships on board
# Different sized ships


# global variables
GRID = 8
USER_BOARD = [[' '] * 8 for i in range(8)]
COMP_BOARD = [[' '] * 8 for i in range(8)]
USER_GUESS_BOARD = [[' '] * 8 for i in range(8)]
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
    while row not in '12345678' or row == '':
        print('Please enter a valid row (1-8) ')
        row = input('Please enter your shot row (1-8): ')
    col = input('Please enter your shot column (A-H): ').upper()
    while col not in 'ABCDEFGH' or col == '':
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


def generate_comp_shot(board):
    '''create computers shot'''
    shot_row, shot_col = random.randint(0, 7), random.randint(0, 7)
    if board[shot_row][shot_col] == 'O':
        board[shot_row][shot_col] = 'X'
        print('Enemy has hit our ship!!!')
        while board[shot_row][shot_col] == 'X':
            shot_row, shot_col = random.randint(0, 7), random.randint(0, 7)
    elif board[shot_row][shot_col] == ' ':
        board[shot_row][shot_col] = '#'
        print('Enemy has missed!!!')
        while board[shot_row][shot_col] == '#':
            shot_row, shot_col = random.randint(0, 7), random.randint(0, 7)


def get_username():
    '''ask user for username'''
    while True:
        username = input('Enter your name: ')
        if len(username) > 20:
            print('Maximum name length is 20 chars')
        elif username == '':
            print('Can not be blank!')
        else:
            break
    return username


def main():
    '''main game function'''
    print('=============================================')
    print('WELCOME TO THE CLASSIC GAME OF BATTLESHIPS!!!')
    print('=============================================\n')
    username = get_username()
    place_ships(USER_BOARD)
    place_ships(COMP_BOARD)
    print(f'\nWelcome to the battle {username}!')
    print('''\n X Marks that ship has been sunk
            \n # Marks that shot has missed it's target
            \n O Marks a ship that has not been sunk yet''')
  
    print(f'\n{username}, This is your game board with your fleet of ships')
    print(' =================')
    print_board(USER_BOARD)
    print(f'\n{username}, This is your enemies board that will mark your shots')
    print(' =================')
    print_board(USER_GUESS_BOARD)
    while True:
        row, col = user_input()
        if COMP_BOARD[row][col] == 'O':
            print(f'\n{username}, You have hit an enemy ship!!!')
            USER_GUESS_BOARD[row][col] = 'X'
            COMP_BOARD[row][col] = 'X'
            generate_comp_shot(USER_BOARD)
        elif COMP_BOARD[row][col] == 'X':
            print(f'\n{username}, You already have sunk a shit at this location')
        elif USER_GUESS_BOARD[row][col] == ' ':
            print(f'\n{username}, You missed!!!')
            generate_comp_shot(USER_BOARD)
            USER_GUESS_BOARD[row][col] = '#'
        elif USER_GUESS_BOARD[row][col] == '#':
            print(f'\n{username}, Shot already has been fired at this location')
        if ships_hit(USER_GUESS_BOARD) == 5:
            print(f'All enemy ships destroyed!!! Congrats!!! {username}  Win!!!')
            break
        elif ships_hit(USER_BOARD) == 5:
            print(f'{username}, Enemy destroyed all your ships, You Lose!!!')
            break
        print(f'\n{username}, This is your game board with your fleet of ships')
        print(' =================')
        print_board(USER_BOARD)
        print(f'\n{username}, This is your enemies board that will mark your shots')
        print(' =================')
        print_board(USER_GUESS_BOARD)


if __name__ == '__main__':
    main()
