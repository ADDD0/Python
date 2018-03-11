def funx():
    x = 5

    def funy():
        nonlocal x
        x += 1
        return x
    return funy


a = funx()
print(a())
print(a())
print(a())
