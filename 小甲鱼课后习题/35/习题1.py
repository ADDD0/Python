# 为04课的猜数小程序加上界面
# 使用try…except语句
import easygui as g
import random

g.msgbox("--------------Let's play a game--------------")
answer = random.randint(1, 10)  # 答案为1~10内的某一随机数字
times = 3  # 初始化计数器
guess = 0

while times >= 0:  # 你甚至可以写成while times + 1:
    title = 'Guess the number'
    if times > 0:
        msg = 'Enter a number which you like from 1 to 10:'
        guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)  # 这里已保证guess为整数

        if guess == answer:  # 先判断是否猜对
            if times == 3:  # 再给出计数器信息
                g.msgbox("Congratulations!You found the right number in only 1 time!\nThat's so cool!", title)
            else:
                g.msgbox("Great!You found the right number in " + str(4 - times) + ' times', title)
            break  # break可以跳出离它最近的while或for循环,这里跳出的循环为第6行的while循环
        else:  # 猜错后给出提示
            if times == 2:
                g.msgbox("That's wrong.You have only 1 time left", title)
            else:
                g.msgbox("That's wrong.You have " + str(times - 1) + " times left", title)
            if times != 1:
                if guess > answer:
                    g.msgbox("Hint:That's a larger one", title)
                else:
                    g.msgbox("Hint:That's a less one", title)
    else:
        g.msgbox("Sorry,you didn't find the right answer,the answer is " + str(answer), title)
        break
    times -= 1
