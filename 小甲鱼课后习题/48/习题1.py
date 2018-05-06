# 写一个迭代器,要求输出至今为止的所有闰年
import time as t


class LeapYears:
    def __init__(self, year=1999):
        self.now = t.localtime()[0]
        self.year = year - 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.year += 1
            if self.year > self.now:
                raise StopIteration
            if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
                return self.year
            else:
                continue


leapyears = LeapYears()
for each in leapyears:
    print(each)
