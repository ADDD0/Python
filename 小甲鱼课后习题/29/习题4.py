# 习题3拓展,用户可以随意输入需要显示的行数
def file_advanced_view(file_name, rows):
    start, end = rows.split(':')

    if start == '':  # 对应情况':?'
        start = '1'
    if end == '':  # 对应情况'?:'
        end = '-1'
    if start == '1' and end == '-1':  # 对应情况':'
        content = 'The full text of the file %s are as follows:' % file_name
    elif start == '1':
        content = 'The contents of file %s from the beginning to %s line are as follows:' \
                  % (file_name, end)
    elif end == '-1':
        content = 'The contents of file %s from %s line to the end are as follows:' \
                  % (file_name, start)
    else:
        content = 'The contents of file %s from %s line to %s line are as follows:' \
                  % (file_name, start, end)
    print(content)

    file = open(file_name)
    lines = int(end) - int(start) + 1  # 输出行数
    if lines < 0:
        print(file.read())
        return
    for i in range(int(start) - 1):  # 读取前面不需要的行,相当于改变指针
        file.readline()
    for j in range(lines):  # 打印目标行
        print(file.readline(), end='')
    file.close()


filename = input('\nPlease enter the file to open:')
row = input('Please enter the number of rows to display[like 3:5 or 3: or:5]:')  # 不建议使用负数,可能会出现bug
file_advanced_view(filename, row)
