def create(file_name):  # Program 1
    file = open(file_name, 'w')
    print("Please enter the content[Enter':w' to save and exit]:")

    while 1:
        content = input('')
        if content != ':w':
            file.write(content + '\n')
        else:
            break

    file.close()


print('----------Create a new file----------')
filename = input('\nPlease enter the file name:')
create(filename)


def compare(first_file_name, second_file_name):  # Program 2
    count = 0
    differ = []
    position = []

    first_file = open(first_file_name)
    second_file = open(second_file_name)

    while True:
        line1 = first_file.readline()
        line2 = second_file.readline()
        count += 1
        if line1 != line2:
            differ.append(count)
            if line1 == '' or line2 == '':
                position.append(1)
            else:
                for each in range(min(len(line1), len(line2))):
                    if line1[each] != line2[each]:
                        position.append(each + 1)
                        break
        if line1 == '' and line2 == '':
            break

    first_file.close()
    second_file.close()

    if differ is False:
        print('The two documents are exactly the same.')
    else:
        print('The difference between the two documents at: %d' % len(differ))
        for each in range(len(differ)):
            print('There are differences in line %s at location %s' % (differ[each], position[each]))


print('----------Determine whether the two documents are the same----------')
firstfilename = input('\nPlease enter the first file name to be compared:')
secondfilename = input('Please enter another file name to be compared:')
compare(firstfilename, secondfilename)


def file_view(file_name, rows):  # Program 3
    print('The first %d lines of the file "%s" are as follows:' % (rows, file_name))
    file = open(file_name)

    while rows:
        print(file.readline(), end='')
        rows -= 1


print('----------Output content----------')
filename = input('\nPlease enter the file to open:')
row = int(input('Please enter the first lines of the file you want to display:'))
file_view(filename, row)


def file_advanced_view(file_name, rows):  # Program 4
    start, end = rows.split(':')

    if start == '':
        start = '1'
    if end == '':
        end = '-1'
    if start == '1' and end == '-1':
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
    lines = int(end) - int(start) + 1
    if lines < 0:
        print(file.read())
        return
    for i in range(int(start) - 1):
        file.readline()
    for j in range(lines):
        print(file.readline(), end='')
    file.close()


print('----------Output any line----------')
filename = input('\nPlease enter the file to open:')
row = input('Please enter the number of rows to display[like 3:5 ot 3: or:5]:')
file_advanced_view(filename, row)


def replace(file_name, org, sub):  # Program 5
    file_read = open(file_name)

    content = []
    count = 0

    for each_line in file_read:
        if org in each_line:
            count = count + each_line.count(org)
            each_line = each_line.replace(org, sub)
        content.append(each_line)

    decide = input('\nThere are {} [{}] in the file {}, '
                   '\nare you sure you want to replace all the [{}] with [{}]?'
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
print('\nThe End')
