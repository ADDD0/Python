# 编写一个Counter类,用于实时检测对象有多少个属性
# 修改以下代码,使之可以正常运行
# class Counter:
#     def __init__(self):
#         self.counter = 0
#
#     def __setattr__(self, key, value):
#         self.counter += 1
#         super().__setattr__(key, value)
#
#     def __delattr__(self, item):
#         self.counter -= 1
#         super().__delattr__(item)


class Counter:
    def __init__(self):
        self.counter = 0

    def __setattr__(self, key, value):
        if key == 'counter':
            return super().__setattr__(key, value)
        else:
            self.counter += 1
            return super().__setattr__(key, value)

    def __delattr__(self, item):
        self.counter -= 1
        return super().__delattr__(item)
