import sys


class Const:
    def __setattr__(self, key, value):
        if not hasattr(self, '%s' % key):
            print('Please set %s attribute first.' % key)
            return None
        elif not key.istitle():
            return super().__setattr__(key, value)
        else:
            print('This is a constant whose value couldn\'t be changed.')
            return None


sys.modules[__name__] = Const()
