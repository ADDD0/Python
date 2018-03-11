result = []


def get_digits(n):
    if n:
        result.insert(0, n % 10)  # 在第一位处插入数字,相当于倒序填入数字
        return get_digits(n // 10)


temp = int(input('Please enter the number:'))
get_digits(temp)
print(result)
