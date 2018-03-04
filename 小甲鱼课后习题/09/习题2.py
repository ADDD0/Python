for i in range(100, 1000):  # 按题目来的暴力解法
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        print(i, end=' ')
print('\n')
total = 0  # 运用本节课知识
for i in range(100, 1000):
    temp = i
    while temp:
        total = total+(temp % 10)**3
        temp //= 10
    if sum == i:
        print(i, end=' ')
