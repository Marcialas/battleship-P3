def user_input():
    while True:
        try:
            row = input('Please enter your shot row (1-8): ')
            if row not in '12345678':
                print('enter valid row')
                continue

            col = input('Please enter your shot column (A-H): ').upper()
            if col not in 'ABCDEFGH':
                print('enter valid letter')
                continue
        except TypeError and ValueError:
            print('erorrrrr')
        return row, col
user_input()
