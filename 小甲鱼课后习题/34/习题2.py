# 使用try…except语句改写第25课习题3
print('''--- Welcome to the address book program ---
--- 1:Query contact information ---
--- 2:Insert a new contact ---
--- 3:Delete existing contacts ---
--- 4:Exit the address book program ---''')
dic = dict()
while 1:
    IC = input('\nPlease enter the relevant instruction code:')

    if IC == '1':
        name = input("Please enter the contact's name:")
        try:
            print(name + ':' + dic[name])
        except KeyError:
            print('Sorry,the program failed to find the contact')
    if IC == '2':
        key = input("Please enter the contact's name:")
        try:
            print('''The name you entered already exists in the address book
-->> %s:%s''' % (key, dic[key]))
            if input('Whether to modify the user information?(y/n)') == 'y':
                dic[key] = input('Please enter the new contact number：')
        except KeyError:
            dic[key] = input('Please enter the user contact number:')
    if IC == '3':
        key = input("Please enter the contact's name:")
        try:
            del(dic[key])
            print('Address book has been successfully emptied')
        except KeyError:
            print('Sorry,the program failed to find the contact')
    if IC == '4':
        break
    else:
        print('You may entered a wrong instruction code.Please enter the correct instruction code')
print('--- Thanks for using address book program ---')
