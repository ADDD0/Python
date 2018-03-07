list1 = []  # 复杂版
for x in range(10):
    for y in range(10):
        if x % 2 == 0:  # 或者if not x % 2:
            if y % 2 != 0:  # 或者if y % 2:
                list1.append((x, y))  # 向列表添加数组对
print(list1)
print([(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0])  # 简易版
print([(x, y) for x in range(0, 10, 2) for y in range(1, 10, 2)])  # 另一简易版
