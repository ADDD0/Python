import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y


class Line:
    def __init__(self, p1, p2):
        self.disX = p1.getx() - p2.getx()
        self.disY = p1.gety() - p2.gety()

    def getlen(self):
        dis = math.sqrt(self.disX**2 + self.disY**2)
        print(dis)
