temp = ['a', 1, 'b', 2, 'c', 3]
count = 0  # Program 1.1
length = len(temp)
while count < length:
    print(temp[count], temp[count+1])
    count += 2
print('')
for each in range(len(temp)):  # Program 1.2
    if each % 2 == 0:
        print(temp[each], temp[each+1])
print('\nThe End')
