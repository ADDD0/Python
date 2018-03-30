# 使用递归算法及欧几里得算法求最大公约数
def gcd(x, y):
    if x % y:
        return gcd(y, x % y)
    else:
        return y


c = int(input('x:'))
d = int(input('y:'))
print(gcd(c, d))
