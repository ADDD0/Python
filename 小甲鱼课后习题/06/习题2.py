# 写一个程序打印出0~100中所有的奇数
a = 1  # 最简便
while a < 100:
    print(a, end=' ')
    a += 2
print('\n')
b = 1  # 运用本节课知识
while b < 100:
    if b % 2 == 1:
        print(b, end=' ')
    else:
        pass
    b += 1
