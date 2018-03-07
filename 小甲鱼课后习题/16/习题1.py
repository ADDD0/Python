def min1(obj):  # 这里为了区分min()函数而在末尾加了个1
    result = obj[0]
    for i in obj:
        if i < result:
            result = i
        else:
            continue
    return result


temp = input('Test min():')  # 你甚至可以输入字符串
print(min1(temp))
