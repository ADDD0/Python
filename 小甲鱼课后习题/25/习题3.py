print('''--- Welcome to the address book program ---
--- 1:Query contact information ---
--- 2:Insert a new contact ---
--- 3:Delete existing contacts ---
--- 4:Exit the address book program ---''')
dic = {}
IC = '0'
while 1:
    IC = input('\nPlease enter the relevant instruction code:')
    if IC == '1':
        if dic == {}:  # 字典中未添加联系人时
            print('Sorry, the program now does not contain any contacts.\nPlease insert a new contact first.')
        else:  # 字典中存在联系人时
            key = input("Please enter the contact's name:")
            if key in dic:  # 查找对象在字典中
                print('%s:%s' % (key, dic[key]))
            if key not in dic:  # 查找对象不在字典中
                jud = input('Sorry,the program failed to find the contact,do you want to create a new contact?(y/n)')
                if jud == 'y':  # 是否创建新的联系人
                    value = input("Please enter the user contact number：")
                    dic[key] = value
    if IC == '2':
        key = input("Please enter the contact's name:")
        if key not in dic:  # 新建联系人不在字典中
            value = input('Please enter the user contact number：')
            dic[key] = value
        else:  # 新建联系人在字典中
            print('''The name you entered already exists in the address book
-->> %s:%s''' % (key, dic[key]))
            jud = input('Whether to modify the user information?(y/n)')
            if jud == 'y':  # 是否修改此联系人信息
                value = input('Please enter the new contact number：')
                dic[key] = value
    if IC == '3':
        dic.clear()
        print('Address book has been successfully emptied.')
    if IC == '4':
        break
    if IC != '1' and IC != '2' and IC != '3' and IC != '4':
        print('You may entered a wrong instruction code.Please enter the correct instruction code.')
if IC == '4':
    print('--- Thanks for using address book program ---')
