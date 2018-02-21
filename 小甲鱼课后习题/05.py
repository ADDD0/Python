number = input('Enter the number which you want to round off:')  # Program 1 四舍五入
while number.isdigit() is False:
    try:
        number = float(number)
    except ValueError:  # 以后可用try，except函数来纠错
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter a floating number:')
    else:
        break
number = float(number)
if number >= 0:
    modified_number = int(number + 0.5)
    print(modified_number)
else:
    modified_number = int(number - 0.5)
    print(modified_number)
print('\n----------Judge leap year----------')  # Program 2 练习题 判断闰年(学过第六课后用取余的方法更为简便)
temp = input('Please enter the year:')
while temp.isdigit() is False or temp == '0':
    temp = input('Sorry "' + temp + '" is not a correct format.\nPlease enter the year:')
year = int(temp)
if year / 400 == int(year / 400):
    print(temp + ' is a leap year')
elif year / 4 == int(year / 4) and year / 100 != int(year / 100):
    print(temp + ' is a leap year.')
else:
    print(temp + ' is not a leap year.')
number = input('\nPlease enter an integer：')  # Program 3 练习题
while number.isdigit() is False or number == '0':
    try:
        0 / int(number)
    except ZeroDivisionError or TypeError:
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter another integer:')
    else:
        break
number = int(number)
if number > 0:
    temp = 1
    while number:
        print(temp)
        temp += 1
        number -= 1
else:
    temp = -1
    while number:
        print(temp)
        temp -= 1
        number += 1
number = input('\nPlease enter an integer：')  # Program 4 练习题(横向)PS：纵向的日后再说
while number.isdigit() is False or number == '0':  # 同Program 3
    if number[1:].isdigit() is False or number == '0':
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter another integer:')
    else:
        break
number = int(number)  # 报错类型为ValueError，格式为‘首位非数字+数字’
if number > 0:
    while number:
        print('!' * int(number), end='')
        print('*' * int(number), end='')
        print()
        number -= 1
else:
    number = int(str(number)[1:])
    while number:
        print('*' * int(number), end='')
        print('!' * int(number), end='')
        print()
        number -= 1
print('\nThe End')
