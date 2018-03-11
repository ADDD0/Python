def fib1(n):  # 递归实现
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):  # 迭代实现(效率高)
    a = b = 1
    while n-2 > 0:
        a, b = b, a + b
        n -= 1
    return b
num = int(input('Please enter the terms:'))
print(fib2(num))
