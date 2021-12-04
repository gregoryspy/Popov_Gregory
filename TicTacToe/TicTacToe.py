WIN_INDEX_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

game_mode = True

def draw_field3(string):
    global game_mode
    print('-' * 19)
    for i in 0, 3, 6:
        line = string[i:i+3]
        print('| ' + ''.join(f'{c:^5}' for c in line) + ' |')
    print('-' * 19)
    x_count = string.count('X')
    o_count = string.count('O')
    if abs(x_count - o_count) >= 2:
        print('Impossible')
    else:
        x_winner, o_winner = False, False
        for wic in WIN_INDEX_COMBINATIONS:
            if all(string[i] == 'X' for i in wic):
                x_winner = True
            if all(string[i] == 'O' for i in wic):
                o_winner = True
        if x_winner and not o_winner:
            print('X wins')
            game_mode = False
        elif not x_winner and o_winner:
            print('O wins')
            game_mode = False
        elif x_winner and o_winner:
            print('Impossible')
        else:
            if string.count('_') > 0:
                print('Game not finished')
            else:
                print('Draw')
                game_mode = False

def game4():
    string = '_' * 9
    symbol = 'X'
    draw_field3(string = string)
    for _ in range(9):
        while True:
            line = input('Enter the coordinates: ')
            try:
                row, col = (int(c) for c in line.split())
            except:
                print('You should enter numbers!')
            else:
                if row not in (1, 2, 3) or col not in (1, 2, 3):
                    print('Coordinates should be from 1 to 3!')
                else:
                    idx = (row - 1) * 3 + col - 1
                    if string[idx] != '_':
                        print('This cell is occupied! Choose another one!')
                    else:
                        print('Ok.')
                        break

        string = string[:idx] + symbol + string[idx + 1:]
        draw_field3(string=string)
        if not game_mode:
            break
        symbol = 'O' if symbol == 'X' else 'X'

if __name__ == '__main__':
    game4()
