# 编写一个程序,接受用户的输入并保存为新的文件(输入:w时结束)
def create(file_name):
    file = open(file_name + '.txt', 'w')
    print("Please enter the content[Enter':w' to save and exit]:")

    while 1:
        content = input('')
        if content != ':w':
            file.write(content + '\n')
        else:
            break

    file.close()


filename = input('\nPlease enter the file name:')
create(filename)
