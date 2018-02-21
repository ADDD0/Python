def outside():  # 调用内部函数
    print('I am outside!')

    def inside():
        print('I am inside!')
    inside()


outside()


def outside():  # 局部变量
    var = 5

    def inside():
        var = 3
        print(var)

    inside()


outside()


def outside():  # 局部变量
    var = 5

    def inside():
        nonlocal var
        print(var)
        var = 8
    inside()


outside()


def funout():  # 访问内部函数
    def funin():
        print('Bingo!You have successfully interviewed me.')
    return funin()


funout()


def funout():  # 访问内部函数
    def funin():
        print('Bingo!You have successfully interviewed me.')
    return funin


funout()()


def funx():
    x = 5

    def funy():
        nonlocal x
        x += 1
        return x
    return funy


a = funx()
print(a())
print(a())
print(a())

str1 = input('Please enter the string:')  # 统计任意字符串字符出现次数(包括空格)
list1 = []
for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n', str1.count(each))
        else:
            print(each, str1.count(each))
        list1.append(each)
print('\nThe End')
