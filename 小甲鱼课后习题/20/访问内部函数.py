def funout():
    def funin():
        print('Bingo!You have successfully interviewed me.')
    return funin()


funout()


def funout():
    def funin():
        print('Bingo!You have successfully interviewed me.')
    return funin


funout()()
