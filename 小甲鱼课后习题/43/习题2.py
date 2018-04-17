# 定义一个单词(Word)类继承自字符串,重写比较操作符,当两个Word类对象进行比较时
# 根据单词的长度来进行比较大小(若字符串带空格,则取第一个空格前的单词作为参数)


class Word(str):
    def __new__(cls, args):
        if ' ' in args:
            args = args[:args.index(' ')]
        return str.__new__(cls, args)  # 将去掉括号的字符串作为新的参数初始化

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) <= len(other)
