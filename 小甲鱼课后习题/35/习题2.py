# 实现一个用于登记用户帐号信息的界面(带*号的为必填项)
# 如*用户名 *手机号码 *E-mail 固定电话 QQ *密码等
# 另存为.txt文件并可以通过"用户名+密码"查找并打印用户帐号信息
import easygui as g

while 1:
    msg = 'Please select the operation you want to perform'
    title = '习题2'
    choice = g.ccbox(msg, title, ('Information registration', 'Information search'))
    title = 'Account center'
    if choice:  # 登记用户帐号信息

        msg = 'Please fill in the contact information'
        fieldNames = ['*用户名', '*手机号码', '*E-mail', '固定电话', 'QQ', '*密码']
        fieldValues = []
        fieldValues = g.multenterbox(msg, title, fieldNames)

        while 1:
            if fieldValues is None:
                break
            errmsg = ''
            for i in range(len(fieldNames)):
                option = fieldNames[i]
                if fieldValues[i] == '' and option[0] == '*':
                    errmsg += '[%s] is required\n\n' % fieldNames[i]
            if errmsg == '':
                with open('用户帐号信息.txt', 'a+', encoding='utf-8') as f:
                    for i in range(len(fieldNames)):
                        f.write('%s:%s ' % (fieldNames[i], fieldValues[i]))
                    f.write('\n')
                break
            fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

    else:  # 查找并打印用户帐号信息

        msg = 'Please enter user name and password'
        fieldNames = ['用户名', '密码']
        fieldValues = []
        fieldValues = g.multenterbox(msg, title, fieldNames)

        # TODO:Use json to solve the problem

    choice = g.ccbox('Do you want to continue?', '习题2')
    if not choice:
        break
