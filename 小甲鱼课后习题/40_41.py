class FileObject:  # Program 1
    def __init__(self, filename='sample.txt'):
        self.new_file = open(filename, 'r')

    def __del__(self):
        self.new_file.close()
        del self.new_file


class C2F(float):  # Program 2
    def __new__(cls, args=0.0):
        return float.__new__(cls, args * 1.8 + 32)


class Nint(int):  # Program 3
    def __new__(cls, args=0):
        if isinstance(args, str):
            temp = 0
            for each in args:
                temp += ord(each)
            args = temp
            return int.__new__(cls, args)
