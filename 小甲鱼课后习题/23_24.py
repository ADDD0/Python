print('Decimal number to binary number')


def dec2bin(dec):  # Program 1 十进制转二进制
    result = ''
    if dec == 0:
        return '0'
    else:
        if dec:
            result = dec2bin(dec // 2)
            return result + str(dec % 2)
        else:
            return result


temp = int(input('Please enter the number:'))
print('0b' + dec2bin(temp))
result2 = []
print('\nSeparate numbers')


def get_digits(n):  # Program 2 分解数字
    if n:
        result2.insert(0, n % 10)
        return get_digits(n // 10)


temp2 = int(input('Please enter the number:'))
get_digits(temp2)
print(result2)


def is_palindrome(n, start, end):  # Program 3 判断回文字符串
    if start > end:
        return 1
    else:
        return is_palindrome(n - 1, start + 1, end - 1) if n[start] == n[end] else 0


string = input('Please enter the string:')
length = len(string) - 1
if is_palindrome(string, 0, length):
    print('\"%s\"is a palindrome.' % string)
else:
    print('\"%s\"is not a palindrome.' % string)
print('\nThe End')
