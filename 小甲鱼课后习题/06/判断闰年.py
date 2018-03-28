temp = input('Please enter the year:')
while temp.isdigit() is False or temp == '0':
    temp = input('Sorry "' + temp + '" is not a correct format.\nPlease enter the year:')
year = int(temp)
if year % 400 == 0:
    print(temp + ' is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print(temp + ' is a leap year')
else:
    print(temp + ' is not a leap year')
