# 编写一个程序,计算2000000以内的素数之和
# 不建议使用列表来存储数列,这个数列很有可能爆掉你的内存
import math as m


def judge(num):  # 不适用于7以内素数求和
    x1 = 7
    x2 = 5
    while True:
        a = b = True
        if x1 < num:
            for i in range(3, int(m.sqrt(x1) + 1), 2):  # 优化了一下课后给出的算法
                if not x1 % i:
                    a = False
                    break
            for i in range(3, int(m.sqrt(x2) + 1), 2):
                if not x2 % i:
                    b = False
                    break
            if a:
                yield x1
            if b:
                yield x2
            x1 += 6
            x2 += 6
        else:
            return 0


def solve(num=10):
    total = 5
    for i in judge(num):
        total += i
    return total


if __name__ == '__main__':
    print(solve())
