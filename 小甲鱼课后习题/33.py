try:  # Programe 1
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i, j)
except KeyboardInterrupt:
    print('Exit.\n')


def int_input(number):  # Program 2
    while 1:
        try:
            print(int(input(number)))
            break
        except ValueError as reason:
            print(reason)


int_input('Please enter an integer:')
print('\nThe End')
