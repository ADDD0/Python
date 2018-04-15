# 写一个程序统计你当前代码量的总和,并显示离十万行代码量还有多远?
# 要求一:递归搜索各个文件夹
# 要求二:显示各个类型的源文件和源代码数量
# 显示总行数与百分比
import easygui as g
import os


def search_code(catalog):
    search_type = ['.c', '.py']
    code_info = {}
    files = {}.fromkeys(search_type, 0)
    lines = {}.fromkeys(search_type, 0)
    for i in os.walk(catalog):  # 通过在目录树中游走输出在目录中的文件名,生成一个迭代器对象
        os.chdir(i[0])  # 每次调用返回一个三元组(当前文件夹路径,子文件夹名,子文件名)
        for each_file in i[2]:
            ext = os.path.splitext(each_file)[1]  # 判断文件扩展名
            if ext in search_type:
                code_info.setdefault(ext, {})  # 发现目标扩展名,键为扩展名,值为一个空字典
                code_line = count_line(each_file)
                code_info[ext].setdefault(each_file, code_line)  # 赋键(文件名)和值(代码行数)给以该扩展名为键的空字典
                files[ext] += 1
                lines[ext] += code_line
    return code_info, files, lines


def count_line(file_name):
    lines = 0
    with open(file_name, errors='ignore') as f:  # 直接忽略掉错误
        for each in f:
            lines += 1
    return lines


def show_result(catalog):
    (code_info, files, lines) = search_code(catalog)
    title = 'Count code amount'
    msg = text = ''
    sumlines = 0
    for ext in code_info:
        for filename in code_info[ext]:
            text += (filename + '  ' + str(code_info[ext][filename]) + '\n')  # 每个文件名及其行数
        if files:
            msg += '{0} {1} files found,code {2} lines\n'.format(files[ext], ext, lines[ext])
            sumlines += lines[ext]
    msg += 'You currently have compiled %d lines of code and completed the progress: %.2f%%\n' \
           'There are %d lines away from 100,000 lines of code. Please continue to work hard!'\
        % (sumlines, sumlines / 1000, 100000 - sumlines)

    os.chdir(catalog)
    choice = []
    for each in os.listdir(os.curdir):  # 对文件或文件夹进行选择
        ext = os.path.splitext(each)[1]
        if ext in code_info:
            choice.append(each)
        if os.path.isdir(each):
            choice.append(each)

    g.textbox(msg, title, text)  # 输出统计信息
    msg = 'Please open the folder or the file you want to view'
    new_path = g.choicebox(msg, title, choice)  # 提供下一个文件或文件夹的选择
    if new_path is not None:
        ext = os.path.splitext(new_path)[1]
        if ext in code_info:
            with open(new_path, encoding='utf-8') as file:  # 显示文件
                title = os.path.basename(new_path)
                msg = 'The contents of file %s are as follows' % title
                text = file.read()
                g.textbox(msg, title, text)
        else:
            new_path = os.getcwd() + os.sep + new_path  # 进行下一次代码统计
            show_result(new_path)


path = g.diropenbox('Please open the folder where you store all the code', '习题5')
show_result(path)
