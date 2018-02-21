number = input('\nPlease enter an integer：')  # Program 1 练习题
while number.isdigit() is False:
    try:
        int(number)
    except ValueError:
        number = input('Sorry "' + number + '" is not a correct format.\nPlease enter another integer:')
number = int(number)
print('Decimal -> Hexadecimal :%d -> 0x%x' % (number, number))  # hex(number)
print('Decimal -> Octal : %d -> 0o%o' % (number, number))  # oct(number)
print('Decimal -> Binary : %d -> ' % number, bin(number))
print('\nThe End')
