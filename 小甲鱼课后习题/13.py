x, y, z = 1, 2, 3  # Program 2
h = x, y, z
print(type(x))
print(type(y))
print(type(z))
print(type(h))
print('')
temp = (x**2 for x in range(5))  # Program 3
for i in range(5):
    print(temp.__next__(), end=' ')
    i += 1
print('\nThe End')
