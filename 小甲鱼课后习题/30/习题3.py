# 输入文件名及开始查找的路径,搜索该文件是否存在
# 若遇到文件夹,则进入文件夹内查找
import os


def search(catalog, target):
    os.chdir(catalog)  # 设定初始查找路径
    for each in os.listdir(os.curdir):
        if each == target:
            print(os.getcwd()+os.sep+each)  # 分别为"当前工作目录","路径分隔符"和"目标文件名"
        if os.path.isdir(each):  # 查找到文件夹
            search(each, target)  # 使用递归,在文件夹中搜索
            os.chdir(os.pardir)  # 检查完后返回上一级目录


Catalog = input('Please enter the initial directory to search:')
Target = input('Please enter the target file to find:')
search(Catalog, Target)
