def gcd1(a, b):  # 辗转相除法(欧几里得算法)
    while b:
        temp = a % b
        a = b
        b = temp
    return a


def gcd2(c, d):  # 更相减损法
    while c != d:
        if c > d:
            c -= d
        else:
            d -= c
    return c


print('Calculate the maximum common divisor of x and y')
x = int(input('x:'))
y = int(input('y:'))
print("It's "+str(gcd1(x, y))+'.')
