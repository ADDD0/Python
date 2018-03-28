# 编写一个程序,判断输入年份是否为闰年
temp = input('Please enter the year:')
while temp.isdigit() is False or temp == '0':  # 这里过滤掉负数和0
    temp = input('Sorry "' + temp + '" is not a correct format.\nPlease enter the year:')
year = int(temp)
if year / 400 == int(year / 400):  # 学过第六课后用取模的方法更为简便
    print(temp + ' is a leap year')
elif year / 4 == int(year / 4) and year / 100 != int(year / 100):
    print(temp + ' is a leap year')
else:
    print(temp + ' is not a leap year')
