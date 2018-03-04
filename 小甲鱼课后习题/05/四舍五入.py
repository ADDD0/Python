number = input('Enter the number which you want to round off:')
while number.isdigit() is False:  # 这里用来判断输入数字是否带负号
    try:
        number = float(number)
    except ValueError:
        number = input('Sorry "'+number+'" is not a correct format.\nPlease enter a floating number:')
    else:
        break
number = float(number)
if number >= 0:
    modified_number = int(number+0.5)
    # int()函数在一定范围内向下取整
    # 尝试int(0.99999999999999994)和int(0.99999999999999995)
    print(modified_number)
else:
    modified_number = int(number-0.5)
    print(modified_number)
