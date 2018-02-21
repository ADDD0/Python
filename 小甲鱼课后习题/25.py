a = dict(one=1, two=2, three=3)  # Program 2
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})
print('--- Welcome to the address book program ---')  # Program 3
print('--- 1:Query contact information ---')
print('--- 2:Insert a new contact ---')
print('--- 3:Delete existing contacts ---')
print('--- 4:Exit the address book program ---')
dic = {}
IC = '0'
while 1:
    IC = input('\nPlease enter the relevant instruction code:')
    if IC == '1':
        if dic == {}:
            print('Sorry, the program now does not contain any contacts.\nPlease insert a new contact first.')
        else:
            key = input("Please enter the contact's name:")
            if key in dic:
                print('%s:%s' % (key, dic[key]))
            if key not in dic:
                jud = input('Sorry,the program failed to find the contact,do you want to create a new contact?(y/n)')
                if jud == 'y':
                    value = input("Please enter the user contact number：")
                    dic[key] = value
    if IC == '2':
        key = input("Please enter the contact's name:")
        if key not in dic:
            value = input("Please enter the user contact number：")
            dic[key] = value
        else:
            print('''The name you entered already exists in the address book
-->> %s:%s''' % (key, dic[key]))
            jud = input('Whether to modify the user information?(y/n)')
            if jud == 'y':
                value = input("Please enter the new contact number：")
                dic[key] = value
    if IC == '3':
        dic.clear()
        print('Address book has been successfully emptied')
    if IC == '4':
        break
    if IC != '1' and IC != '2' and IC != '3' and IC != '4':
        print('You may entered a wrong instruction code.Please enter the correct instruction code.')
if IC == '4':
    print('--- Thanks for using address book program ---')
print('\nThe End')
