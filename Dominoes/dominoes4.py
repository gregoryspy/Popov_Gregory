import random
from itertools import combinations_with_replacement

STATUS_COMP = 'computer'
STATUS_PLAYER = 'player'

def get_pieces():
    pieces = [(p1, p2) for p1, p2 in combinations_with_replacement(range(7), 2)]
    random.shuffle(pieces)
    return pieces

def draw():
    print('=' * 70)
    print('Stock size:', len(stock_pieces))
    print('Computer pieces:', len(computer_pieces))
    if len(snake) <= 6:
        print(''.join(piece_str(p) for p in snake))
    else:
        print(''.join(piece_str(p) for p in snake[:3]) + '...' + ''.join(piece_str(p) for p in snake[-3:]))
    print('Your pieces:')
    for i, p in enumerate(player_pieces, start=1):
        print(f'{i}: {piece_str(p)}')
    if status == STATUS_PLAYER:
        print('Status: It\'s your turn to make a move. Enter your command.')
    else:
        print('Status: Computer is about to make a move. Press Enter to continue...')

def piece_str(piece):
    return f'[{piece[0]},{piece[1]}]'


if __name__ == '__main__':

    while True:
        stock_pieces = get_pieces()
        computer_pieces, player_pieces = [], []
        for _ in range(7):
            computer_pieces.append(stock_pieces.pop())
            player_pieces.append(stock_pieces.pop())
        doubles1 = [p for p in computer_pieces if p[0]==p[1]]
        doubles2 = [p for p in player_pieces if p[0]==p[1]]
        if doubles1 or doubles2:
            break

    snake = max(doubles2 + doubles1)
    if snake in computer_pieces:
        status = STATUS_PLAYER
        computer_pieces.pop(computer_pieces.index(snake))
    else:
        status = STATUS_COMP
        player_pieces.pop(player_pieces.index(snake))
    snake = [snake]
    while True:
        draw()
        if status == STATUS_COMP:
            input()
            while True:
                move = random.choice(range(-len(computer_pieces), len(computer_pieces)+1))
                if move == 0:
                    print('computer missed move...')
                    if stock_pieces:
                        rnd_piece = random.choice(stock_pieces)
                        computer_pieces.append(stock_pieces.pop(stock_pieces.index(rnd_piece)))
                    break
                else:
                    piece_move = computer_pieces[abs(move) - 1]
                    if move < 0:
                        if snake[0][0] in piece_move:
                            piece_move = computer_pieces.pop(computer_pieces.index(piece_move))
                            if piece_move[0] == snake[0][0]:
                                piece_move = tuple(reversed(piece_move))
                            snake = [piece_move] + snake
                            break
                    if move > 0:
                        if snake[-1][-1] in piece_move:
                            piece_move = computer_pieces.pop(computer_pieces.index(piece_move))
                            if piece_move[1] == snake[-1][-1]:
                                piece_move = tuple(reversed(piece_move))
                            snake = snake + [piece_move]
                            break

        else:
            while True:
                try:
                    move = int(input())
                except:
                    print('Incorrect move! Try again')
                else:
                    if move not in range(-len(player_pieces), len(player_pieces)+1):
                        print('Incorrect move! Try again')
                    else:
                        if move == 0:
                            rnd_piece = random.choice(stock_pieces)
                            player_pieces.append(stock_pieces.pop(stock_pieces.index(rnd_piece))) #!!!!!
                            break
                        else:
                            piece_move = player_pieces.pop(abs(move) - 1)
                            if move < 0:
                                if snake[0][0] in piece_move:
                                    if piece_move[0] == snake[0][0]:
                                        piece_move = tuple(reversed(piece_move))
                                    snake = [piece_move] + snake
                                    break
                                else:
                                    print('Illegal move. Please try again.')
                            if move > 0:
                                if snake[-1][-1] in piece_move:
                                    if piece_move[1] == snake[-1][-1]:
                                        piece_move = tuple(reversed(piece_move))
                                    snake = snake + [piece_move]
                                    break
                                else:
                                    print('Illegal move. Please try again.')

        if len(computer_pieces) == 0:
            print('Status: The game is over. The computer won!')
            break
        if len(player_pieces) == 0:
            print('Status: The game is over. You won!')
            break
        if snake[0][0] == snake[-1][-1] and [p[0] for p in snake].count(snake[0][0]) + [p[1] for p in snake].count(snake[0][0]) == 8:
            print('Status: The game is over. It\'s a draw!')
            break

        status = STATUS_COMP if status == STATUS_PLAYER else STATUS_PLAYER


