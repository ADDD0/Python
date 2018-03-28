# 编程实现sum()
def sum1(obj):
    result = 0
    for i in obj:
        if i.isnumeric() is True:  # 在isdigit,isdecimal和isnumeric中isnumeric判定范围最广
            i = int(i)
            result += i
        else:
            continue
    return result


temp = input('Test sum():')
print(sum1(temp))
