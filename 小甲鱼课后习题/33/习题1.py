# 请恢复以下代码中遗漏的代码,使得程序执行后可以按要求输出
# try:                                 print: 0  0
#   for i in range(3):                        0  1
#       for j in range(3):                    0  2
#           __________                        1  0
#               _______________________       1  1
#           print(i, j)                       1  2
# except KeyboardInterrupt:                   Exit
#     print('Exit')
try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i, j)
except KeyboardInterrupt:
    print('Exit')
