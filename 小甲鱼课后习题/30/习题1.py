# 统计任意目录下各个文件类型的数目
import os


def num(catalog):
    file = os.listdir(catalog)  # 列出当前文件夹下的所有文件(夹)名
    # 这里的查找机制为查找"."号并输出其至名称末尾的所有字符
    type_ext = {}
    for i in file:
        extension_name = os.path.splitext(i)[1]  # 得到扩展名
        if extension_name == '':
            extension_name = 'folder'  # 没有扩展名就默认为文件夹(后面会学习其他更加准确的方法)
            type_ext.setdefault(extension_name, 0)  # 设定键和初始值
        else:
            type_ext.setdefault(extension_name, 0)
        type_ext[extension_name] += 1
    for each in type_ext.keys():
        print(each+':'+str(type_ext[each]))


num(input('Please enter the directory to search:'))
