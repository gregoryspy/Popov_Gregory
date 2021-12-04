import argparse
from math import ceil, log, floor

ERR_MSG = 'Incorrect parameters'

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)

args = parser.parse_args()
type = args.type
loan = args.principal
months = args.periods
rate = args.interest
if rate:
    rate = rate / 100 / 12
mp = args.payment

# print(type, loan, months, rate)
# print(args)

if (loan is not None and loan < 0) or (months is not None and months < 0) or (rate is not None and rate < 0):
    print(ERR_MSG)

elif type == 'diff':
    if loan and months and rate and not mp:
        s = 0
        for m in range(months):
            mp1 = ceil(loan / months + rate * (loan - (loan * (m)) / (months)))
            print(f'Month {m+1:0>2}: payment is {mp1}')
            s = s + mp1
        overpay = int(s - loan)
        print(f'Overpayment = {overpay}')
    else:
        print(ERR_MSG)

elif type == 'annuity':
    if loan and months and rate and not mp:
        mp = ceil(loan * rate * (1 + rate) ** months / ((1 + rate) ** months - 1))
        overpay = int(mp * months - loan)
        print(f'Your annuity payment = {mp}!')
        print(f'Overpayment = {overpay}')
    elif not loan and months and rate and mp:
        loan = floor(mp * ((1 + rate) ** months - 1) / (rate * (1 + rate) ** months))
        overpay = int(mp * months - loan)
        print(f'Your loan principal = {loan}!')
        print(f'Overpayment = {overpay}')
    elif loan and not months and rate and mp:
        months = ceil(log(mp / (mp - rate * loan), rate + 1))
        overpay = int(mp * months - loan)
        if months >= 12:
            years, months = months // 12, months % 12
            if not months:
                print(f'It will take {years} years to repay the loan!')
            else:
                print(f'It will take {years} years and {months} months to repay the loan!')
        else:
            print(f'It will take {months} months to repay the loan!')
        print(f'Overpayment = {overpay}')
    else:
        print(ERR_MSG)

else:
    print(ERR_MSG)
