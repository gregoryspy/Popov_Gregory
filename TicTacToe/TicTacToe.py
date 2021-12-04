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
