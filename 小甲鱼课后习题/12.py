list1 = []  # Program 2.1 复杂版
for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                list1.append((x, y))
print(list1)
print('')
print([(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0])  # Program 2.2 简易版
print('')
print([(x, y) for x in range(0, 10, 2) for y in range(1, 10, 2)])  # Program 2.3 目标版
print('\nThe End')
