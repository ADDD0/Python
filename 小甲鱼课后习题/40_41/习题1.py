# 写一个FileObject类,包装文件对象,删除对象时文件能自动关闭


class FileObject:
    def __init__(self, filename='sample.txt'):
        self.new_file = open(filename, 'r')

    def __del__(self):
        self.new_file.close()
        del self.new_file
