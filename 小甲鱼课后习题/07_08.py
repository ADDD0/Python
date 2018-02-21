[x, y, z] = input('Please enter 3 integers from 0~9 which you manage(no space):')
y, x, z = z, y, x
print(x, y, z)  # 此篇开始无特殊要求不编写关于格式错误的问题了
x = int(x)
y = int(y)
z = int(z)
small = x if x < y and x < z else y if y < z else z  # 尝试下min函数
print('\nThe smallest one is '+str(small)+' .')
print('\nThe End')
