a = 1  # Program 1.1 练习题(最简便)
while a < 100:
    print(a, end=' ')
    a += 2
print('\n')
b = 1  # Program 1.2 练习题(运用本节课知识)
while b < 100:
    if b % 2 == 1:
        print(b, end=' ')
    else:
        pass
    b += 1
print('')
c = 7  # Program 2 练习题
while c < 100:
    if c % 2 == 1 and c % 3 == 2 and c % 5 == 4 and c % 6 == 5 and c % 7 == 0:
        print(c, end=' ')
    else:
        pass
    c += 7
print('\n----------Judge leap year----------')  # Program 3 练习题 判断闰年
temp = input('Please enter the year:')
while temp.isdigit() is False or temp == '0':
    temp = input('Sorry "'+temp+'" is not a correct format.\nPlease enter the year:')
year = int(temp)
if year % 400 == 0:
    print(temp+' is a leap year')
elif year % 4 == 0 and year % 00 != 0:
    print(temp+' is a leap year.')
else:
    print(temp+' is not a leap year.')
print('\nThe End')
