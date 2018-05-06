# 增加描述符的功能:使用文件来存储属性
# 如果属性被删除了,文件也会同时被删除
import time as t
import pickle
import os


class Record:
    def __init__(self, value, record):
        self.value = value
        self.record = record

    def __get__(self, instance, owner):
        try:
            with open('record.txt', 'a') as f:
                time = t.asctime(t.localtime())
                f.write('The {0} variable was read at {1}, {0} = {2}\n'.format(self.record, time, self.value))
        except AttributeError as r:
            print('{0}, please set the variable first'.format(r))
            return None
        try:
            p = open('{0}.pkl'.format(self.record), 'rb')
            self.value = pickle.load(p)
            return self.value
        except OSError as r:
            print('{0}, please set the variable {1} first'.format(r, self.record))
            return None

    def __set__(self, instance, value):
        self.value = value
        with open('record.txt', 'a') as f:
            time = t.asctime(t.localtime())
            f.write('The {0} variable was modified at {1}, {0} = {2}\n'.format(self.record, time, self.value))
        with open('{0}.pkl'.format(self.record), 'wb') as p:  # 使用文件来存储属性
            pickle.dump(self.value, p)

    def __delete__(self, instance):
        with open('record.txt', 'a') as f:  # 记录删除操作
            time = t.asctime(t.localtime())
            f.write('The {0} variable was deleted at {1}\n'.format(self.record, time))
        os.remove('{0}.pkl'.format(self.record))  # 删除文件
        del self.record  # 删除属性


class Test:
    x = Record(10, 'x')
    y = Record('Python', 'y')
