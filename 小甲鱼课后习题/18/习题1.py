def test(*var, base=3):
    result = 0
    for i in var:
        result += i
    result *= base
    return result


print(test(2, 3, 4, base=5))
