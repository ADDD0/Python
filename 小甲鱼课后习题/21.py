print(list(filter(lambda x: not(x % 3), range(1, 101))))  # Program 1
print(list(map(lambda x, y: [x, y], range(1, 10, 2), range(2, 11, 2))))  # Program 2
print('\nThe End')
