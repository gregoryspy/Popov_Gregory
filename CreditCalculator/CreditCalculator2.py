from math import ceil

loan = int(input('Enter the loan principal:\n< '))

txt_option = '''What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:
> '''

option = input(txt_option)

if option == 'm':
    mp = int(input('Enter the monthly payment:\n> '))
    months = ceil(loan / mp)
    print(f'It will take {months} months to repay the loan')

if option == 'p':
    months = int(input('Enter the number of months:\n> '))
    if loan % months == 0:
        mp = loan // months
        print(f'Your monthly payment = {mp}')
    else:
        mp = ceil(loan / months)
        lp = loan - mp * (months - 1)
        print(f'Your monthly payment = {mp} and the last payment = {lp}')