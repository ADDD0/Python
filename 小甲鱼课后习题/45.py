class C:
    def __getattr__(self, item):
        print(1)

    def __getattribute__(self, item):
        print(2)

    def __setattr__(self, key, value):
        print(3)

    def __delattr__(self, item):
        print(4)


c = C()
c.x = 1  # What will be displayed here?
print(c.x)  # What will be displayed here?


class C:
    def __getattr__(self, item):
        print(1)
        return super().__getattr__(item)

    def __getattribute__(self, item):
        print(2)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print(3)
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print(4)
        return super().__delattr__(item)


c = C()
c.x  # What will be displayed here?
dir(super)


class Counter:  # Wrong
    def __init__(self):
        self.counter = 0

    def __setattr__(self, key, value):
        self.counter += 1
        super().__setattr__(key, value)

    def __delattr__(self, item):
        self.counter -= 1
        super().__delattr__(item)


class Counter:  # Correct
    def __init__(self):
        self.counter = 0

    def __setattr__(self, key, value):
        if key == 'counter':
            return super().__setattr__(key, value)
        else:
            self.counter += 1
            return super().__setattr__(key, value)

    def __delattr__(self, item):
        self.counter -= 1
        return super().__delattr__(item)
