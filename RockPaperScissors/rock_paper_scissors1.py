ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
OPTIONS = (ROCK, PAPER, SCISSORS)

class RockPaperScissorsGame:
    def __init__(self):
        self.player_move = None
        self.computer_move = None

    def get_player_move(self):
        choice = input('> ')
        for option in OPTIONS:
            if option.lower().startswith(choice.lower()):
                return option


    def get_computer_move(self, player_move):
        idx = OPTIONS.index(player_move)
        return OPTIONS[(idx + 1) % len(OPTIONS)]

    def show_player_lose(self, computer_move):
        print(f'Sorry, but the computer chose {computer_move}')

    def start(self):
        pm = self.get_player_move()
        cm = self.get_computer_move(player_move=pm)
        self.show_player_lose(computer_move=cm)

if __name__ == '__main__':
    game = RockPaperScissorsGame()
    game.start()
