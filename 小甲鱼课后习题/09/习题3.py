for red in range(1, 4):  # 循环嵌套
    for yellow in range(1, 4):
        for green in range(2, 7):
            if red+yellow+green == 8:
                print('red\t'*red+'yellow\t'*yellow+'green\t'*green)  # \t代表缩进
