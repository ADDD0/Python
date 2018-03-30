# 使用递归算法摸拟pow()
def power(x, y):
    if y:
        return x * power(x, y - 1)
    else:
        return 1


a = int(input('for x ='))
b = int(input('for y ='))
print(power(a, b))
