# 利用filter()和lambda表达式快速求出100以内所有3的倍数
print(list(filter(lambda x: not(x % 3), range(1, 101))))
