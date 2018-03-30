# 统计字符串的英文字母,空格,数字和其它字符的个数


def statistics(*string):  # 输入参数不唯一
    for j in string:
        letters = 0
        digits = 0
        spaces = 0
        others = 0
        for i in j:
            if i.isalpha():
                letters += 1
            elif i.isnumeric():
                digits += 1
            elif i == ' ':
                spaces += 1
            else:
                others += 1

        print('There are %s alphabets,%s numbers,%s blanks and %s special characters' %
              (letters, digits, spaces, others))


statistics('Hello World!', 'I love Python.')
