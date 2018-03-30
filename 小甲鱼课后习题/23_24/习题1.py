# 使用递归编写一个十进制转换为二进制的函数
def dec2bin(dec):
    result = ''
    if dec == 0:
        return '0'
    if dec == 1:
        return '1'
    else:
        if dec:
            result = dec2bin(dec // 2)
            return result + str(dec % 2)
        else:
            return result


temp = int(input('Please enter the number:'))
print(dec2bin(temp))
