import random
answer = random.randint(1, 10)  # 答案为1~10内的某一随机数字
print("--------------Let's play a game--------------")
times = 3  # 初始化计数器
guess = 0
while times >= 0:  # 你甚至可以写成while times+1:
    if times > 0:
        guess = input('Enter a number which you like from 1 to 10:')
        while guess.isdigit() is False:  # str.isdigit()用于判断字符串是否只包含数字
            # 这里也可以写成while not guess.isdigit():
            print('\nSorry "'+str(guess)+'" is not a correct format.Please enter an integer.')
            guess = input('Enter an "integer" which you like from 1 to 10:')
        guess = int(guess)
        if guess == answer:  # 先判断是否猜对
            if times == 3:  # 再给出计数器信息
                print("Congratulations!You found the right number in only 1 time!\nThat's so cool!")
            else:
                print("Great!You found the right number in "+str(4-times)+' times.')
            break  # break可以跳出离它最近的while或for循环，这里跳出的循环为第6行的while循环
        else:  # 猜错后给出提示
            if times == 2:
                print("That's wrong.You have only 1 time left.")
            else:
                print("That's wrong.You have "+str(times-1)+" times left.")
            if guess > answer:
                print("Hint:That's a larger one.\n")
            else:
                print("Hint:That's a less one.\n")
    else:
        print("Sorry,you didn't find the right answer,the answer is "+str(answer)+' .')
        break
    times -= 1
