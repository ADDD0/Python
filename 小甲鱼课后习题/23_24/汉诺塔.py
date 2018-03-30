def hanoi(n, a, b, c):
    if n == 1:
        print(a + '->' + c)  # 将第一根柱子上的盘子移动到第三根柱子上
    else:
        hanoi(n - 1, a, c, b)  # 将第一根柱子上的前n-1个盘子移动到第二根柱子上
        print(a + '->' + c)  # 将第一根柱子上的第n个盘子移动到第三根柱子上
        hanoi(n - 1, b, a, c)  # 将第二根柱子上的n个盘子(即第一根柱子上的前n-1个盘子)移动到第三根柱子上


layer = int(input("Please enter the hanoi's layers:"))
hanoi(layer, 'a', 'b', 'c')
