# 定义一个Nstr类,支持字符串的相减操作:A-B,从A中去除所有B的子字符串


class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')
