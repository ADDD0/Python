def min1(obj):  # Program 1
    result = obj[0]
    for i in obj:
        if i < result:
            result = i
        else:
            continue
    return result


temp = input('Test min():')
print(min1(temp))


def sum1(obj):  # Program 2
    result = 0
    for i in obj:
        if i.isnumeric() is True:
            i = int(i)
            result += i
        else:
            continue
    return result


temp = input('\nTest sum():')
print(sum1(temp))
print('\nThe End')
