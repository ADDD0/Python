# 计算任意文件夹大小
import os


def getdirsize(catalog):
    file = os.listdir(catalog)
    size = 0
    for i in file:
        if os.path.isdir(os.path.join(catalog, i)):
            getdirsize(os.path.join(catalog, i))  # 递归调用
        else:
            size += os.path.getsize(os.path.join(catalog, i))
    print(os.path.basename(catalog) + ':' + str(size) + 'Bytes')


getdirsize(input('Please enter the directory to search:'))
