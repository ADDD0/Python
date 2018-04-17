class C:
    def __getattr__(self, item):
        print(1)

    def __getattribute__(self, item):
        print(2)

    def __setattr__(self, key, value):
        print(3)

    def __delattr__(self, item):
        print(4)


c = C()
c.x = 1  # 这里会显示什么?
print(c.x)  # 这里会显示什么?
