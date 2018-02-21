class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')

    def __lshift__(self, other):
        return self[other:]+self[:other]

    def __rshift__(self, other):
        return self[:-other]+self[-other:]


class Nstr2(str):
    def __init__(self, arg=''):
        super(Nstr2, self).__init__()  # 求解释
        if isinstance(arg, str):
            self.ascii = 0
            for each in arg:
                self.ascii += ord(each)
        else:
            print('Wrong parameters.')

    def __add__(self, other):
        return self.ascii + other.ascii

    def __sub__(self, other):
        return self.ascii - other.ascii

    def __mul__(self, other):
        return self.ascii * other.ascii

    def __truediv__(self, other):
        return self.ascii / other.ascii
