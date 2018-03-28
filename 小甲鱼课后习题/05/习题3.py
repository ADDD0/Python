# 实现以下功能
# >>>输入一个整数:3
# >>>   ***
#      **
#     *
number = input('Please enter an integer:')
while number.isdigit() is False or number == '0':  # 这里用了一个巧妙的方法来检验输入数字是否为非零整数
    try:
        0 / int(number)
    except ZeroDivisionError or TypeError:
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter another integer:')
    else:
        break
number = int(number)
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
