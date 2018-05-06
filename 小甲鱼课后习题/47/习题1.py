# 定制一个列表,要求实现以下要求:
# (1)实现获取,设置和删除一个元素的行为(删除元素的时候对应的计数器也会被删除)
# (2)增加counter(index)方法,返回index函数所指定的元素记录的访问次数
# (3)实现append(),pop(),remove(),insert(),clear()和reverse()方法


class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in range(len(args)):
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, item):
        self.count[item] += 1
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        self.count[key] = 0
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def __reversed__(self):
        self.count.reverse()
        super().__reversed__()

    def counter(self, index):
        return self.count[index]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, index=-1):
        del self.count[index]
        return super().pop(index)

    def remove(self, value):
        del self.count[super().index(value)]
        super().remove(value)

    def insert(self, index, value):
        self.count.insert(index, 0)
        super().insert(index, value)

    def clear(self):
        self.count = []
        super().clear()
