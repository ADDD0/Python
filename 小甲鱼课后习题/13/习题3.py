temp = (x**2 for x in range(5))  # 这里的temp是一个迭代器
for i in range(5):
    print(temp.__next__(), end=' ')  # 每次运行可以得到一个值
    i += 1
