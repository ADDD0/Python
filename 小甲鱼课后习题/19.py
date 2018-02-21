print('----------Judge the palindrome----------')  # Program 1.1 判断回文联
a = input('Please enter the string:')
b = len(a)


def judge(ordinery_string, length):
    if length == 1 or 0:
        print('%s is a palindrome.' % ordinery_string)
    else:
        i = 0
        while length > i:
            if ordinery_string[length - 1] == ordinery_string[i]:
                length -= 1
                i += 1
                if length - i == 1 or 0:
                    print('%s is a palindrome.' % ordinery_string)
            else:
                print('Sorry,%s is not a palindrome.' % ordinery_string)
                break


judge(a, b)
# def judge(ordinery_string):  # Program 1.2 简易方法
#     list1 = list(ordinery_string)
#     list2 = list.reverse(ordinery_string)
#     if list1 == list2:
#         print('%s is a palindrome.' % ordinery_string)
#     else:
#         print('Sorry,%s is not a palindrome.' % ordinery_string)
print('\n--------Statistics string parameters--------')  # Program 2 判断字符串参数个数
temp = list(input('Please enter the string:'))
a = input(':').split()
print(a)


def statistics(*string):
    temp1 = 0
    temp2 = 0
    temp3 = 0
    temp4 = 0
    for i in string:
        if i.isalpha():
            temp1 += 1
        else:
            continue
    for i in string:
        if i.isnumeric():
            temp2 += 1
        else:
            continue
    for i in string:
        special_characters = '~!@#$%^&*()_=-/,.?<>;:[]{}\|'
        if i in special_characters:
            temp3 += 1
        else:
            continue
    for i in string:
        if i == ' ':
            temp4 += 1
    print('There are %s alphabets,%s numbers,%s special characters and %s blanks.' %
          (temp1, temp2, temp3, temp4))


statistics(temp)
print('\nThe End')
