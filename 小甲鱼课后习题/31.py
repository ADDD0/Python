import pickle


def save_file(boy, girl, count):
    file_name_boy = 'boy_'+str(count)+'.txt'
    file_name_girl = 'girl_'+str(count)+'.txt'

    boy_file = open(file_name_boy, 'wb')
    girl_file = open(file_name_girl, 'wb')

    pickle.dump(boy, boy_file)
    pickle.dump(girl, girl_file)

    boy_file.close()
    girl_file.close()


def split_file(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'A':
                boy.append(line_spoken)
            if role == 'B':
                girl.append(line_spoken)
        else:
            save_file(boy, girl, count)

            boy = []
            girl = []
            count += 1
    save_file(boy, girl, count)

    f.close()


split_file('29.txt')
print('\nSave completed.')
print('\nThe End')
