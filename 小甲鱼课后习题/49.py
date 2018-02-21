import math as m


def judge(num):  # 不适用于7以内素数求和
    x1 = 7
    x2 = 5
    while True:
        a = b = True
        if x1 < num:
            for j in range(3, int(m.sqrt(x1)+1), 2):  # 优化了一下课后给出的解法
                if not x1 % j:
                    a = False
                    x1 += 6
                    break
            for j in range(3, int(m.sqrt(x2)+1), 2):
                if not x2 % j:
                    b = False
                    x2 += 6
                    break
            if a:
                yield x1
                x1 += 6
            if b:
                yield x2
                x2 += 6
        else:
            return 0


def solve(num=2000000):
    total = 5
    for i in judge(num):
        total += i
    return total


if __name__ == '__main__':
    print(solve())
