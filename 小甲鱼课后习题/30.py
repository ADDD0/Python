import os


def add_up():  # Program 1
    file = os.listdir(os.curdir)
    type_ext = {}
    for i in file:
        extension_name = os.path.splitext(i)[1]
        if extension_name == '':
            extension_name = 'folder'
            type_ext.setdefault(extension_name, 0)
        else:
            type_ext.setdefault(extension_name, 0)
        type_ext[extension_name] += 1
    for each in type_ext.keys():
        print(each+':'+str(type_ext[each]))


print('----------Statistics file types and their number----------')
add_up()
print('\n')


def size():  # Program 2
    file = os.listdir(os.curdir)
    for i in file:
        file_size = os.path.getsize(os.getcwd() + '/' + i)
        print(i+':'+str(file_size)+'Bytes')


print('-------Statistics of the current directory of the file size-------')
size()
print('\n')


def search(catalog, target):  # Program 3
    os.chdir(catalog)
    for each in os.listdir(os.curdir):
        if each == target:
            print(os.getcwd() + os.sep + each)
        if os.path.isdir(each):
            search(each, target)
            os.chdir(os.pardir)


print('----------Find a directory of the specified file----------')
Catalog = input('Please enter the initial directory to search:')
Target = input('Please enter the target file to find:')
search(Catalog, Target)
print('\n')


def search_video(catalog):  # Program 4
    os.chdir(catalog)

    for each in os.listdir(os.curdir):
        if os.path.splitext(each)[1] in search_type:
            video_path.append(os.getcwd() + os.sep + each + os.linesep)
        if os.path.isdir(each):
            search_video(catalog + os.sep + each)
            os.chdir(os.pardir)


print('-----Find all the video files in the path and generate a VideoList file-----')
search_type = ['.mp4', '.rmvb', '.avi']
video_path = []

Catalog = input('Please enter the initial directory to search:')
search_video(Catalog)

os.chdir(Catalog)
f = open('VideoList.txt', 'w')
f.writelines(video_path)
f.close()
print('Program 4 accomplished.\n')


def search_keyword(catalog, keyword):  # Program 5
    os.chdir(catalog)

    for each_file in os.listdir(os.curdir):
        if os.path.splitext(each_file)[1] == '.txt' or os.path.splitext(each_file)[1] == '.py':
            file = open(os.getcwd() + os.sep + each_file, encoding='UTF-8')
            end = file.seek(0, 2)
            file.seek(0, 0)
            count_lines = 0
            emerge = []
            position = {}
            judge = False
            line = ''
            while True:
                count_lines += 1
                try:
                    line = file.readline()
                except UnicodeDecodeError:
                    pass
                if keyword in line:
                    emerge.append(count_lines)
                    position[count_lines] = findstr(line, keyword)
                    judge = True
                if file.tell() == end:  # 这里的end感觉像黑科技一样，不能直接用if file.tell() == file.seek(0, 2)
                    break
            if judge:
                print('Find the keywords [{}] in the file [{}]\n'
                      .format(keyword, os.getcwd() + os.sep + each_file))
                for each in emerge:
                    print('The keyword appears on line {},location{}\n'
                          .format(each, position[each]))
                print('==================================================')
            file.close()

        if os.path.isdir(each_file):
            search_keyword(catalog + os.sep + each_file, keyword)
            os.chdir(os.pardir)


def findstr(enter, check):  # 等一个正则表达式
    count = 0
    length_c = len(check)
    length_e = len(enter)
    initial = check[0]
    last_letter = check[length_c - 1]
    output = []
    if check not in enter:
        return
    elif length_c == 1:
        for each in enter:
            if each == check:
                count += 1
        return print(count)
    else:
        for each in range(length_e - length_c + 1):
            if enter[each] == initial and enter[each + length_c - 1] == last_letter:
                if enter[each:(each + length_c)] == check:
                    output.append(each + 1)
        return output


print('-----Find all text files that contain keywords in the current folder-----')
Catalog = input('Please enter the initial directory to search:')
Keyword = input('Please enter the keywords you want to find:')
search_keyword(Catalog, Keyword)
print('\nThe End.')
