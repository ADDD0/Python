# 用户输入关键字,查找当前文件夹内(包含子文件夹)所有含有该关键字的文本文件(.txt后缀)
# 要求显示该文件所在的位置以及关键字在文件中的具体位置
import os


def search_files(catalog):
    for i in os.walk(catalog):  # 通过在目录树中游走输出在目录中的文件名,生成一个迭代器对象
        os.chdir(i[0])  # 每次调用返回一个三元组(当前文件夹路径,子文件夹名,子文件名)
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt' or os.path.splitext(each_file)[1] == '.py':
                search_in_file(each_file, Keyword)


def search_in_file(file_name, keyword):  # 查找文件中的每一行
    lines = {}
    count = 0
    with open(file_name, errors='ignore') as f:  # 直接忽略掉错误
        for each_line in f:
            count += 1
            if keyword in each_line:
                lines.setdefault(count, pos_in_line(each_line, keyword))
        if lines != {}:
            print('Find keyword [%s] in file [%s]' % (Keyword, os.getcwd() + os.sep + file_name))
            for i in lines.keys():
                print('Line %s, position %s' % (i, lines[i]))


def pos_in_line(line, keyword):  # 输出每一行关键字的位置
    positions = []
    pos = line.find(keyword)
    while pos != -1:
        positions.append(pos)
        pos = line.find(keyword, pos + 1)
    return positions


Catalog = input('Please enter the initial directory to search:')
Keyword = input('Please enter the keywords you want to find:')
search_files(Catalog)
