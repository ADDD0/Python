# 编写一个程序,当用户输入文件名和行数(n)后,将该文件的前n行内容打印
def file_view(file_name, rows):
    print('The first %d lines of the file "%s" are as follows:' % (rows, file_name))
    file = open(file_name)

    while rows:
        print(file.readline(), end='')  # 不加end=''的话会自动换行
        rows -= 1


filename = input('\nPlease enter the file to open:')
row = int(input('Please enter the first lines of the file you want to display:'))
file_view(filename, row)
