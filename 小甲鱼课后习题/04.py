import random  # 猜数字
times = 3
answer = random.randint(1, 10)
print("--------------Let's play a game--------------")
guess = 0
while guess != answer and times >= 0:
    if times > 0:
        guess = input('Enter a number which you like from 1 to 10:')
        while guess.isdigit() is False:
            print('\nSorry "'+str(guess)+'" is not a correct format.Please enter an integer.')
            guess = input('Enter an "integer" which you like from 1 to 10:')
        guess = int(guess)
        if guess == answer:
            if times == 3:
                print("Congratulations!You found the right number in only 1 time!\nThat's so cool!")
            else:
                print("Great!You found the right number in "+str(4-times)+' times.')  # 尝试下格式化字符
            break
        else:
            if times == 2:
                print("That's wrong.You have only 1 time left.")
            else:
                print("That's wrong.You have "+str(times-1)+" times left.")
            if guess > answer:
                print("Hint:That's a larger one.\n")
            else:
                    print("Hint:That's a less one.\n")
    else:
        print("Sorry,you didn't find the right answer,the answer is " + str(answer) + ' .')
        break
    times -= 1
print('\nThe End')
