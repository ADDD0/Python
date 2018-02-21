def test(*var, base=3, temp=0):  # Program 1
    if var[-1] == 5:
        base = 5
        var = var[:-1]
    for i in var:
        temp += i
    temp *= base
    return print(temp)


test(1, 2, 3, 4, 5)  # 带逗号的字符串如何转化为带逗号的整型格式？？？？


def findstr(enter, check):  # Program 2.1 检查任意字符串并输出个数
    count = 0
    length_c = len(check)
    length_e = len(enter)
    initial = check[0]
    last_letter = check[length_c - 1]
    if check not in enter:
        print('Sub string is not found in the target string.')
        return
    elif length_c == 1:
        for each in enter:
            if each == check:
                count += 1
        return print(count)
    else:
        for each in range(length_e - length_c + 1):
            if enter[each] == initial and enter[each + length_c - 1] == last_letter:
                if enter[each:(each + length_c)] == check:
                    count += 1
        return print(count)


enter_ = input('Please enter the target string:')
check_ = input('Please enter the sub string:')

findstr(enter_, check_)  # Program 2.2 简易版
print(enter_.count(check_))
print('\nThe End')
