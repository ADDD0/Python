# 定义一个点(Point)类和直线(Line)类,使用getlen方法可以获得直线的长度
# 提示:设点A(x1,y1),点B(x2,y2),则两点构成的线段长度|AB|=sqrt((x1-x2)²+(y1-y2)²)
#      Python中计算开根号可使用math模块中的sqrt函数
#      直线由两点构成,因此初始化时需有两个点(Point)对象作为参数
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
        dis = math.sqrt(self.disX ** 2 + self.disY ** 2)
        print(dis)
