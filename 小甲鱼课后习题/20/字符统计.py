str1 = input('Please enter the string:')
list1 = []
for each in str1:
    if each not in list1:
        print(each, str1.count(each))
        list1.append(each)
