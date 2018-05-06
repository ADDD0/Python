# 编写描述符Record:记录指定变量的读取和写入操作
# 并将记录以及触发时间保存到文件:record.txt
import time as t


class Record:
    def __init__(self, value, record):
        self.value = value
        self.record = record

    def __get__(self, instance, owner):
        try:
            with open('record.txt', 'a') as f:  # 记录读取操作
                time = t.asctime(t.localtime())
                # time.localtime([secs])接收时间辍(1970纪元年后经过的浮点秒数)并返回当地时间下的时间元组t
                # time.asctime([t])接收时间元组并返回一个可读的形式为"Sun May  6 10:10:29 2018"
                # (2018年5月6日 周日 10时10分29秒)的24个字符的字符串
                f.write('The {0} variable was read at {1}, {0} = {2}\n'.format(self.record, time, self.value))
        except AttributeError as r:
            print('{0}, please set the variable first'.format(r))
            return None
        try:
            return self.value
        except AttributeError as r:
            print('{0}, please set the variable {1} first'.format(r, self.record))
            return None

    def __set__(self, instance, value):
        self.value = value
        with open('record.txt', 'a') as f:  # 记录写入操作
            time = t.asctime(t.localtime())
            f.write('The {0} variable was modified at {1}, {0} = {2}\n'.format(self.record, time, self.value))


class Test:
    x = Record(10, 'x')
    y = Record('Python', 'y')
