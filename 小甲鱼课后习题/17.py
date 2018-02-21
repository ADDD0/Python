def gcd1(x, y):  # Program 2.1 辗转相除法（欧几里得算法）
    while y:
        temp = x % y
        x = y
        y = temp
    return x


def gcd2(x, y):  # Program 2.2 更相减损法
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


print('Calculate the maximum common divisor of x and y')
x = int(input('x:'))
y = int(input('y:'))
print("It's " + str(gcd1(x, y)) + '.')


def dec2bin(x):  # Program 3 bin()
    temp1 = []
    temp2 = ''
    while x:
        a = x % 2
        x //= 2
        temp1.append(a)
    while temp1:
        temp2 += str(temp1.pop())
    return temp2


print('\nDecimal number to binary number')
x = int(input(':'))
print("It's " + str(dec2bin(x)) + '.')
print('\nThe End')
