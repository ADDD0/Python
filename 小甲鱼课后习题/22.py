print('---imitate the built-in-function "power(x, y)"---')


def power(x, y):  # Program 1 使用递归算法摸拟bif_pow()
    if y:
        return x * power(x, y - 1)
    else:
        return 1


a = int(input('for x ='))
b = int(input('for y ='))
print(power(a, b))
print('\n---Calculate the maximum common divisor of x and y---')


def gcd(x, y):  # Program 2 使用递归算法及欧几里得算法求最大公约数
    if x % y:
        return gcd(y, x % y)
    else:
        return y


c = int(input('x:'))
d = int(input('y:'))
print(gcd(c, d))
print('\nThe End')
