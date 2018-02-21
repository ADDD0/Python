class C:  # Program 1
    count = 0

    def __init__(self):
        C.count += 1

    def __del__(self):
        C.count -= 1


class Stack:  # Program 2
    def __init__(self, start):
        if start is None:
            start = []
        self.stack = []
        for x in start:
            self.push(x)

    def isempty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print('Warning!The stack is empty!')
        else:
            return self.stack.pop()

    def top(self):
        if not self.stack:
            print('Warning!The stack is empty!')
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print('Warning!The stack is empty!')
        else:
            return self.stack[0]
