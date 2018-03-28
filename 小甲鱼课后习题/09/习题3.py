# 12个仅颜色不同的球,3红3黄6绿,从中任意摸出8个球,编程计算摸出球的各种颜色搭配
for red in range(1, 4):  # 循环嵌套
    for yellow in range(1, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print('red\t' * red + 'yellow\t' * yellow + 'green\t' * green)  # \t代表缩进
