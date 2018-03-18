def file_view(file_name, rows):
    print('The first %d lines of the file "%s" are as follows:' % (rows, file_name))
    file = open(file_name, encoding='utf-8')

    while rows:
        print(file.readline(), end='')  # 不加end=''的话会自动换行
        rows -= 1


print('----------Output content----------')
filename = input('\nPlease enter the file to open:')
row = int(input('Please enter the first lines of the file you want to display:'))
file_view(filename, row)
