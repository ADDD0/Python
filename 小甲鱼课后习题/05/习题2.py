number = input('Please enter an integer：')
while number.isdigit() is False or number == '0':
    if number[0] == '-' and number[1:].isdigit() is True:  # 这里增加了输入为负数的情况,检验方法为直接验证
        break
    else:
        number = input('Sorry "'+number+'" is not a correct format.\nPlease enter another integer:')
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
