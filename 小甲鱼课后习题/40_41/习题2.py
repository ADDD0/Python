# 定义一个类实现摄氏度到华氏度的转换(华氏度=摄氏度*1.8+32)


class C2F(float):
    def __new__(self, args=0):
        super(C2F, self).__new__()
        return float.__new__(self, args * 1.8 + 32)
