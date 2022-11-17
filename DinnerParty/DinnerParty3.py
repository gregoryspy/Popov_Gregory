from math import ceil
import random

if __name__ == '__main__':
    n = int(input('Enter the number of friends joining (including you):\n> '))
    if n == 0:
        print('No one is joining for the party')
    else:
        print('Enter the name of every friend (including you), each on a new line:')
        friends = {}
        for _ in range(n):
            friends[input('> ')] = 0
        amount = float(input('Enter the total amount:\n> '))
        amount_per_friend = ceil(amount / len(friends) * 100) / 100
        for key in friends:
            friends[key] = amount_per_friend
        # print(friends)
        choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')
        if choice.lower() == 'yes':
            lucky = random.choice(list(friends.keys()))
            print(f'{lucky} is the lucky one!')
        else:
            print('No one is going to be lucky')