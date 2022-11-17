import random
from itertools import combinations_with_replacement

STATUS_COMP = 'computer'
STATUS_PLAYER = 'player'

def get_pieces():
    pieces = [(p1, p2) for p1, p2 in combinations_with_replacement(range(7), 2)]
    random.shuffle(pieces)
    return pieces


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
    print('Stock pieces:', stock_pieces)
    print('Computer pieces:', computer_pieces)
    print('Player pieces:', player_pieces)
    print('Domino snake:', snake)
    print('Status:', status)

