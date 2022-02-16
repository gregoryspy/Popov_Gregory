import random

RIGHT, WRONG = 'right!', 'wrong!'
INCORRECT = 'Incorrect format'
correct_answers = 0
level_complexity = 0
FILENAME = 'results.txt'


def get_expression():
    if level_complexity == 1:
        a, b = (random.randint(2, 9) for _ in range(2))
        operation = random.choice('+*')
        expression = f'{a} {operation} {b}'
        return expression
    if level_complexity == 2:
        a = random.randint(11, 29)
        expression = f'{a}'
        return expression

def setup_level():
    global level_complexity
    msg = '''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29'''
    while True:
        print(msg)
        choice = input('> ')
        if choice in ('1', '2'):
            level_complexity = int(choice)
            break
        else:
            print(INCORRECT)


def is_correct(expression, answer):
    if level_complexity == 1:
        return eval(expression) == answer
    if level_complexity == 2:
        return eval(expression + '** 2') == answer



def get_answer():
    got = input('> ')
    return int(got)

def save_results():
    print('Would you like to save the result? Enter yes or no.')
    if input('> ').lower() == 'yes':
        name = input('What is your name?\n> ')
        with open(FILENAME, 'a') as f:
            f.write(f'{name}: {correct_answers}/5\n')


def main():
    global correct_answers
    setup_level()
    for i in range(5):
        expression = get_expression()
        print(expression)
        while True:
            try:
                answer = get_answer()
                if is_correct(expression=expression, answer=answer):
                    print(RIGHT + '\n')
                    correct_answers += 1
                else:
                    print(WRONG + '\n')
                break
            except ValueError:
                print(INCORRECT)
    print(f'Your mark is {correct_answers}/5.')
    save_results()


if __name__ == '__main__':
    main()
