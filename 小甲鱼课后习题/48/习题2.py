# 写一个MyRev类,功能与reversed()相同


class MyRev:
    def __init__(self, args=None):
        self.rev = args + args[-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.rev = self.rev[:-1]
            return self.rev[-1]
        except IndexError:
            raise StopIteration


myrev = MyRev('nohtyP')
for each in myrev:
    print(each, end='')
