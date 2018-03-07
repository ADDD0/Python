temp = ['a', 1, 'b', 2, 'c', 3]
count = 0  # 复杂解法
length = len(temp)
while count < length:
    print(temp[count], temp[count+1])
    count += 2
print('')
for each in range(len(temp)):  # 另一个复杂解法
    if each % 2 == 0:
        print(temp[each], temp[each+1])
# 学完25课后可用字典实现
