f = open(r'文件.txt', 'w')
f.write('I\nLove\nPython')
f = open(r'文件.txt', 'r')
for each in f:  # 这里输出有空行是因为换行符\n也被当做一个字符来看待，每打印一个换行符就出现了一段空行
    print(each)
f.close()
