# 用户输入关键字,查找当前文件夹内(包含子文件夹)所有含有该关键字的文本文件(.txt后缀)
# 要求显示该文件所在的位置以及关键字在文件中的具体位置
# 附加要求:可以更改查找到的关键字
import os


def pos_in_line(line, keyword):
    positions = []
    pos = line.find(keyword)
    while pos != -1:
        positions.append(pos)
        pos = line.find(keyword, pos+1)
    print('Position %s' % positions)


def search_in_file(file_name, keyword):
    count = 0
    f = open(file_name, encoding='utf-8', errors='ignore')
    for each_line in f:
        count += 1
        if keyword in each_line:
            print('Find keyword [%s] in file [%s]' % (Keyword, file_name))
            print('Line %s' % count)
            pos_in_line(each_line, keyword)
        print('Find keyword [%s] in file [%s]' % (Keyword, file_name))


def search_files(catalog):
    for i in os.walk(catalog):
        os.chdir(i[0])
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt' or os.path.splitext(each_file)[1] == '.py':
                search_in_file(each_file, Keyword)


Catalog = input('Please enter the initial directory to search:')
Keyword = input('Please enter the keywords you want to find:')
search_files(Catalog)
