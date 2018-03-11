print('---imitate the built-in-function "power(x, y)"---')


def power(x, y):  # 使用递归算法摸拟pow()
    if y:
        return x * power(x, y-1)
    else:
        return 1


a = int(input('for x ='))
b = int(input('for y ='))
print(power(a, b))
