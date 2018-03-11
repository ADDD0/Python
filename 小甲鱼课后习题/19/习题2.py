print('--------Statistics string parameters--------')  # Program 2 判断字符串参数个数


def statistics(*string):
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

        print('There are %s alphabets,%s numbers,%s blanks and %s special characters.' %
              (letters, digits, spaces, others))


statistics('Hello World!', 'I love Python.')
