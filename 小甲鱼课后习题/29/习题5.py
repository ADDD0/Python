def replace(file_name, org, sub):
    file_read = open(file_name)

    content = []
    count = 0

    for each_line in file_read:
        if org in each_line:
            count = count + each_line.count(org)  # 用于统计替换字符总数
            each_line = each_line.replace(org, sub)
        content.append(each_line)  # 用于记录所有行(包括替换的和未替换的)

    decide = input('\nThere are {} [{}] in the file {}, '
                   '\nare you sure to replace all the [{}] with [{}]?'
                   '\n[Y/N]:'.format(count, org, file_name, org, sub))
    if decide == 'Y':
        file_write = open(file_name, 'w')
        file_write.writelines(content)
        file_write.close()
    file_read.close()


print('----------Replace function----------')
filename = input('\nPlease enter the file to open:')
original = input('Please enter the words or characters that need to be replaced:')
substitute = input('Please enter the new words or characters:')
replace(filename, original, substitute)
