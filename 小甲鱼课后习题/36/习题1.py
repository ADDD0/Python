# 按照以下提示尝试定义一个矩形类并生成类实例对象
# 属性:长和宽
# 方法:设置长和宽-->setRect(self)
#      获得长和宽-->getRect(self)
#      获得面积-->getArea(self)


class Rectangle:
    length = 5
    width = 4

    def setrect(self):
        print('Please enter the length and width of the rectangle')
        self.length = float(input('length:'))
        self.width = float(input('width:'))

    def getrect(self):
        print('The rectangle\'s length is %.2f, width is %.2f' % (self.length, self.width))

    def getarea(self):
        print('The rectangle\'s area is %.2f' % (self.length * self.width))


rect = Rectangle()
print('Now you can call the class instance object"rect"')
