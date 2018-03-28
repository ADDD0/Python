# 编写一个进制转换程序
number = input('Please enter an integer：')
while number.isdigit() is False:  # 可以输入负数
    if '.' in number:  # 去掉小数
        raise TypeError
    try:
        int(number)
    except ValueError:
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter another integer:')
number = int(number)
print('Decimal -> Hexadecimal :%d -> 0x%x' % (number, number))  # hex(number)十六进制转换
print('Decimal -> Octal : %d -> 0o%o' % (number, number))  # oct(number)八进制转换
print('Decimal -> Binary : %d -> ' % number, bin(number))  # 二进制转换
