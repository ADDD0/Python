# 编写一个新的函数int_input(),当用户输入整数的时候正常返回,否则提示出错并要求重新输入
def int_input(number):
    while 1:
        try:
            print(int(input(number)))
            break
        except ValueError as reason:
            print(reason)


int_input('Please enter an integer:')
