# 写一个矩形类,默认有宽和高两个属性
# 如果为一个叫square的属性赋值,那么说明这是一个正方形
# 值就是正方形的边长,此时宽和高都应该等于边长


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.width = self.height = value
        else:
            self.name = value


r = Rectangle(3, 4)
# 看似正确,实则会导致无限递归
# 因为赋值时会一直调用__setattr__()函数而无法得到返回值
# 解决方案：
# ①else下改为super().__setattr__(name, value) 调用基类方法
# ②else下改为self.__dict__[name] = value 修改实例的字典属性
