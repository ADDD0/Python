c = 7
while c < 1000:
    if c % 2 == 1 and c % 3 == 2 and c % 5 == 4 and c % 6 == 5 and c % 7 == 0:
        print(c, end=' ')
    else:
        pass
    c += 7
