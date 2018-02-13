print("---Let's play a game---")  # Program 1 比大小
temp = input('Press a number which you like:')
guess = int(temp)
if guess >= 319099:
    print("It's a big one.")
else:
    print("It's a small one.")

temp = input('\nPlease enter your name：')  # Program 2 练习题
print('Hello，'+temp+'!')  # 以后可以试试格式化字符串
print('\nThe End')
