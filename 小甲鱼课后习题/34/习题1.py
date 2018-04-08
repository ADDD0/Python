# 使用with语句改写第29课习题2
# 删去了某些功能,主要区别在于文件的打开和关闭上
def compare(file1, file2):
    with open(file1, encoding='utf-8') as f1, open(file2, encoding='utf-8') as f2:
        count = 0
        differ = []

        for line1 in f1:
            line2 = f2.readline()
            count += 1
            if line1 != line2:
                differ.append(count)
    return differ


first = input('Please enter the first file name to be compared:')
second = input('Please enter another file name to be compared:')
differs = compare(first, second)

if len(differs) == 0:
    print('The two documents are exactly the same')
else:
    print('The difference between the two documents at: %d' % len(differs))
    for each in range(len(differs)):
        print('There are differences in line %s' % (differs[each]))
