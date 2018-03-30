# 尝试编写一个用户登录程序(尝试将功能封装成函数)
data = {}


def menu():
    order = input('''|---Create user:N/n---|
|---Log in account:E/e---|
|---Exit the program:Q/q---|
\nPlease enter the relevant instruction code:''')
    while len(order) != 1 or order not in 'NnEeQq':
        order = input('''You may entered a wrong instruction code.
Please enter the correct instruction code:''')
    if order == 'N' or order == 'n':
        add()
    if order == 'E' or order == 'e':
        log_in()
    if order == 'Q' or order == 'q':
        return


def add():
    key = input('Please enter user name:')
    while key in data:  # 新建用户名已被占用时
        key = input('Username %s already exists, please re-enter:' % key)
    value = input('Please enter the password:')
    data[key] = value
    print('Registration success')
    menu()


def log_in():
    if data == {}:  # 字典中未添加用户时
        print('Sorry, the program is not logged in by anyone.\nPlease create a new user first')
        menu()
    count = 3
    while count:  # 三次错误机会
        key_ = input('Please enter user name:')
        value_ = input('Please enter the password:')
        if key_ in data and value_ == data[key_]:  # 用户登录成功
            print('Sign in successfully')
            return menu()       
        print('''The user name does not exist or the password is incorrectly entered.
Please re-enter the user name and password.
The time you can re-enter:%d''' % (count-1))
        count -= 1
    print('Login failed')
    return menu()


menu()
