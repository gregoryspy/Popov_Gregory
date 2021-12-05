
if __name__ == '__main__':
    n = int(input('Enter the number of friends joining (including you):\n> '))
    if n == 0:
        print('No one is joining for the party')
    else:
        print('Enter the name of every friend (including you), each on a new line:')
        friends = {}
        for _ in range(n):
            friends[input('> ')] = 0
        print(friends)