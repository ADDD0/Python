# 这里以timeit模块为例
import timeit

print(timeit.__doc__)  # 查看模块简介
print('*' * 60)
print(dir(timeit))  # 返回参数的属性,方法列表
print('*' * 60)
print(timeit.__all__)
# 如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量
# 那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入
print('*' * 60)
print(timeit.__file__)  # 返回源代码位置
print('*' * 60)
print(help(timeit))  # help()函数用于查看函数或模块用途的详细说明
