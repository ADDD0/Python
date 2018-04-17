# 定义一个类继承于int类型,并实现功能:当传入的参数为字符串时,返回
# 该字符串中所有字符的ASCII码的和(使用ord()获得一个字符的ASCII码的值)


class Nint(int):
    def __new__(cls, args=0):
        if isinstance(args, str):
            temp = 0
            for each in args:
                temp += ord(each)
            args = temp
            return int.__new__(cls, args)
