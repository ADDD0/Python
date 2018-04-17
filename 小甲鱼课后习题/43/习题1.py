# 定义一个类C,当实例化该类的时候,自动判断传入了多少个参数并显示出来


class C:
    def __init__(self, *args):
        if not args:
            print('No parameter')
        else:
            print('parameter:{} name:'.format(len(args)), end='')
            for each in args:
                print(each, end=' ')
