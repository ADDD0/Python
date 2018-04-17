# 在一个类中定义一个变量,用于跟踪该类有多少个实例被创建
# (当实例化一个对象时,这个变量+1,当销毁一个对象时,这个变量-1)


class C:
    count = 0

    def __init__(self):
        C.count += 1

    def __del__(self):
        C.count -= 1
