x, y, z = input('Please enter 3 integers from 0~9 which you manage(no space):')
y, x, z = z, y, x  # 顺序改变
print(x, y, z)  # 此篇开始无特殊要求不再编写关于格式错误的问题
x = int(x)
y = int(y)
z = int(z)
small = x if x < y and x < z else y if y < z else z  # 尝试下min函数small = min(x, y ,z)
print('\nThe smallest one is '+str(small)+' .')
