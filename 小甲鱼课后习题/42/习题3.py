# 定义一个Nstr类,当该类的实例对象间发生的加,减,乘,除运算时
# 将该对象的所有字符串的ASCII码之和进行计算


class Nstr(str):
    def __init__(self, arg=''):
        super(Nstr, self).__init__()
        # 此句可加可不加,不加会显示一个缺少父类初始化的弱警报
        if isinstance(arg, str):
            self.ascii = 0
            for each in arg:
                self.ascii += ord(each)
        else:
            print('Wrong parameters')

    def __add__(self, other):
        return self.ascii + other.ascii

    def __sub__(self, other):
        return self.ascii - other.ascii

    def __mul__(self, other):
        return self.ascii * other.ascii

    def __truediv__(self, other):
        return self.ascii / other.ascii

    def __floordiv__(self, other):
        return self.ascii // other.ascii
