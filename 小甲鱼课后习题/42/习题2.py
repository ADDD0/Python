# 定义一个Nstr类,支持移位操作符的运算(左移和右移)


class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[:-other] + self[-other:]
