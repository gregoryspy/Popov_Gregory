

def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()



