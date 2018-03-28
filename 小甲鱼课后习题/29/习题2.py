def compare(first_file_name, second_file_name):
    count = 0
    differ = []
    position = []

    first_file = open(first_file_name)
    second_file = open(second_file_name)

    while True:
        line1 = first_file.readline()
        line2 = second_file.readline()
        count += 1
        if line1 != line2:  # 文件不相同时
            differ.append(count)
            if line1 == '' or line2 == '':  # 若其中一行为空
                position.append(1)  # 位置为1
            else:
                for each in range(min(len(line1), len(line2))):  # 从开头到较短行的所有索引位置
                    if line1[each] != line2[each]:  # 判断每个字符是否相同
                        position.append(each+1)
                        break
        if line1 == '' and line2 == '':  # 文件末尾均为空字符
            break

    first_file.close()
    second_file.close()

    if differ is False:  # 即differ为空列表时
        print('The two documents are exactly the same.')
    else:
        print('The difference between the two documents at: %d' % len(differ))  # 统计不同行的数量
        for each in range(len(differ)):
            print('There are differences in line %s at location %s' % (differ[each], position[each]))


print('----------Determine whether the two documents are the same----------')
first = input('\nPlease enter the first file name to be compared:')
second = input('Please enter another file name to be compared:')
compare(first, second)
