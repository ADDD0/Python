def outside():
    var = 5

    def inside():
        var = 3
        print(var)
    inside()


outside()


def outside():
    var = 5

    def inside():
        nonlocal var
        print(var)
        var = 8
    inside()


outside()
