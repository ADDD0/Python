# 创建一个const模块,让Python支持常量(无法修改的变量,如True,False,None等)
# 提示:
# 1.我们需要一个const类
# 2.重写Const类的某一个魔法方法,指定当实例对象的属性被修改时的行为
# 3.检查该属性是否已存在
# 4.属性名大写时被定义成常量
# 5.使用以下方法可以将你的模块与类A的对象挂钩
#     import sys
#     sys.modules[__name__] = A()
#   sys.modules是一个字典,它包含了从Python开始运行起被导入的所有模块
#   键就是模块名,值就是模块对象
import sys


class Const:
    def __setattr__(self, key, value):
        if not hasattr(self, '%s' % key):
            print('Please set %s attribute first' % key)
            return None
        elif not key.istitle():
            return super().__setattr__(key, value)
        else:
            print("This is a constant whose value can't be changed")
            return None


sys.modules[__name__] = Const()
