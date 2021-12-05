from math import ceil

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
        print(friends)