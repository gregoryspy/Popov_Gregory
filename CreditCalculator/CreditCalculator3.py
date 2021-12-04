from math import ceil, log, floor


txt_option = '''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> '''

option = input(txt_option)

if option == 'n':
    loan = float(input('Enter the loan principal:\n< '))
    mp = int(input('Enter the monthly payment:\n> '))
    rate = float(input('Enter the loan interest:\n> ')) / 100 / 12
    months = ceil(log(mp / (mp - rate * loan), rate + 1))
    if months >= 12:
        years, months = months // 12, months % 12
        if not months:
            print(f'It will take {years} years to repay the loan!')
        else:
            print(f'It will take {years} years and {months} months to repay the loan!')
    else:
        print(f'It will take {months} months to repay the loan!')

if option == 'a':
    loan = float(input('Enter the loan principal:\n< '))
    months = int(input('Enter the number of periods:\n> '))
    rate = float(input('Enter the loan interest:\n> ')) / 100 / 12
    mp = ceil(loan * rate * (1 + rate) ** months / ((1 + rate) ** months - 1))
    print(f'Your monthly payment = {mp}!')

if option == 'p':
    mp = float(input('Enter the annuity payment:\n> '))
    months = int(input('Enter the number of periods:\n> '))
    rate = float(input('Enter the loan interest:\n> ')) / 100 / 12
    loan = floor(mp * ((1 + rate) ** months - 1) / (rate * (1 + rate) ** months))
    print(f'Your loan principal = {loan}!')



