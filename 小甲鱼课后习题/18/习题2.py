def findstr(enter, check):  # 检查任意字符串并输出个数
    count = 0
    length_e = len(enter)
    length_c = len(check)
    initial = check[0]  # 定义要查找的初始字符
    last_letter = check[length_c-1]  # 定义要查找的结束字符
    if check not in enter:  # 判断原字符串是否包含目标字符串
        print('Sub string is not found in the target string.')
        return
    elif length_c == 1:  # 对单个字符的查找
        for i in enter:
            if i == check:
                count += 1
        return count
    else:
        for i in range(length_e-length_c+1):  # 对初始字符的查找范围
            if enter[i] == initial and enter[i+length_c-1] == last_letter:  # 检查前后字符是否相同
                if enter[i:(i+length_c)] == check:  # 检查整个字符串是否相同
                    count += 1
        return count


enter_ = input('Please enter the target string:')
check_ = input('Please enter the sub string:')

print(findstr(enter_, check_))
print(enter_.count(check_))  # 简易版
