def dec2bin(x):  # 实现bin()
    temp = binary = ''
    while x:
        a = x % 2
        x //= 2
        temp += str(a)
    for i in reversed(temp):  # 这里的reversed(temp)是一个迭代器,每进行一次读取操作可以输出一个字符
        binary += i
    return binary


number = int(input('Decimal number to binary number:'))
print("It's "+dec2bin(number)+'.')
