bill = input('How much is your bill?:')
pymt = input('How much is your payment?:')
change = float(pymt) - float(bill);

print('Hi! Your change is ' + str(change))