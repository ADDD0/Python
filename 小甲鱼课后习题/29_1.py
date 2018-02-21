f = open('29.txt')

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
        file_name_boy = 'boy_' + str(count) + '.29.txt'
        file_name_girl = 'girl_' + str(count) + '.29.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy_' + str(count) + '.29.txt'
file_name_girl = 'girl_' + str(count) + '.29.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()
print('\nSave completed.')
