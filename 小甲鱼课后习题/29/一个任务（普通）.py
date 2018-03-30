# 将文件('对话.txt')中的数据进行分割并按照以下规律保存起来
# -A的对话单独保存为boy_*.txt文件(去掉"A:")
# -B的对话单独保存为girl_*.txt文件(去掉"B:")
# -将3段对话分别保存为boy_1.txt,girl_1.後,…共8个文件
f = open('对话.txt')

boy = []
girl = []
count = 1

for each_line in f:  # 这里的each_line为str类型
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':', 1)  # 以冒号为分隔符,最多分为两段
        if role == 'A':
            boy.append(line_spoken)
        if role == 'B':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')  # 如果输出为乱码的话尝试修改一下文件编码为gbk
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1
f.close()
print('\nSave completed')
