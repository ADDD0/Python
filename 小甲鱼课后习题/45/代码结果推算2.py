class C:
    def __getattr__(self, item):
        print(1)
        return super().__getattr__(item)

    def __getattribute__(self, item):
        print(2)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print(3)
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print(4)
        return super().__delattr__(item)


c = C()
print(dir(super))
print(c.x)  # 这里会显示什么?
