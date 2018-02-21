class C:
    def __init__(self, *args):
        if not args:
            print('No parameter.')
        else:
            print('parameter:{} name:'.format(len(args)), end='')
            for each in args:
                print(each, end=' ')


class Word(str):
    def __new__(cls, args):
        if ' ' in args:
            args = args[:args.index(' ')]
        return str.__new__(cls, args) # ????

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) <= len(other)
