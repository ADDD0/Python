def create(file_name):
    file = open(file_name+'.txt', 'w')
    print("Please enter the content[Enter':w' to save and exit]:")

    while 1:
        content = input('')
        if content != ':w':
            file.write(content+'\n')
        else:
            break

    file.close()


print('----------Create a new file----------')
filename = input('\nPlease enter the file name:')
create(filename)
