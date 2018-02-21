class Rectangle:
    length = 5
    width = 4

    def setRect(self):
        print('Please enter the length and width of the rectangle')
        self.length = float(input('length:'))
        self.width = float(input('width:'))

    def getRect(self):
        print('The rectangle\'s length is %.2f, width is %.2f.' % (self.length, self.width))

    def getArea(self):
        print('The rectangle\'s area is %.2f' % (self.length * self.width))

rect = Rectangle()
print('Now you can call the class instance object"rect".')
