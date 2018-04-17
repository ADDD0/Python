import time as t
import pickle
import os


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
        return float(instance.cel*1.8 + 32)

    def __set__(self, instance, value):
        self.value = float(value)
        instance.cel = (value - 32)/1.8


class Temperature:
    cel = Celsius()
    fah = Fahrenheit()


class Record:
    def __init__(self, value, record):
        self.value = value
        self.record = record

    def __get__(self, instance, owner):
        try:
            with open('record.txt', 'a') as f:
                time = t.asctime(t.localtime())
                f.write('The {0} variable was read at {1}, {0} = {2}'.format(self.record, time, self.value))
                f.write('\n')
        except AttributeError as r:
            print('{0}, please set the variable first.'.format(r))
            return None
        try:
            p = open('{0}.pkl'.format(self.record), 'rb')
            self.value = pickle.load(p)
            return self.value
        except OSError as r:
            print('{0}, please set the variable {1} first.'.format(r, self.record))
            return None

    def __set__(self, instance, value):
        self.value = value
        with open('record.txt', 'a') as f:
            time = t.asctime(t.localtime())
            f.write('The {0} variable was modified at {1}, {0} = {2}'.format(self.record, time, self.value))
            f.write('\n')
        with open('{0}.pkl'.format(self.record), 'wb') as p:
            pickle.dump(self.value, p)

    def __delete__(self, instance):
        with open('record.txt', 'a') as f:
            time = t.asctime(t.localtime())
            f.write('The {0} variable was deleted at {1}'.format(self.record, time))
            f.write('\n')
        os.remove('{0}.pkl'.format(self.record))
        del self.record


class Test:
    x = Record(10, 'x')
    y = Record('Python', 'y')
