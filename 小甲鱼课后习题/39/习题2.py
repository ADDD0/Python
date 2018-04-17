# 定义一个栈(Stack)类,用于模拟一种具有后进先出(LIFO)特性的数据结构,至少需要有以下方法:
# isempty()  判断当前栈是否为空
# push()     往栈的顶部压入一个数据项
# pop()      从栈顶弹出一个数据项(并在栈中删除)
# top()      显示当前栈顶的一个数据项
# bottom()   显示当前栈底的一个数据项


class Stack:
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
