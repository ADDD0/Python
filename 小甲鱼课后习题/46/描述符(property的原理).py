# 先定义一个温度类,然后定义两个描述符类用于描述摄氏度和华氏度两个属性
# 要求两个属性会自动进行转换,即一个属性值改变,另一个属性值也改变


class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __init__(self, value=78.8):
        self.value = value

    def __get__(self, instance, owner):
        return float(instance.cel * 1.8 + 32)

    def __set__(self, instance, value):
        self.value = float(value)
        instance.cel = (value - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()
