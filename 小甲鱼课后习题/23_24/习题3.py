# 使用递归函数判断回文字符串
def palindrome(n, start, end):
    if start > end:
        return 1
    else:
        return palindrome(n, start + 1, end - 1) if n[start] == n[end] else 0


string = input('Please enter the string:')
length = len(string)-1
if palindrome(string, 0, length):
    print('\"%s\"is a palindrome.' % string)
else:
    print('\"%s\"is not a palindrome.' % string)
