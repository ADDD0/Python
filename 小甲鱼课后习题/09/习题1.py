# 设计一个验证用户密码程序,用户只有三次机会输入,不过如果用户输入的内容中包含"*"则不计算在内
import random
prime_number = [2, 3, 5, 7]  # 猜密码(猜数字升级版)
number = 0
for i in range(2, 100):  # 得到100以内所有质数
    if i % 2 and i % 3 and i % 5 and i % 7 != 0:
        prime_number.append(i)
        number += 1
    else:
        continue
    # 第49课利用迭代器得到质数且算法进行了优化
answer = prime_number[random.randint(0, number + 4)]  # 这里加4是为了算上最开始的2357
# 或者用random.choice(prime_number)
guess = 1
time = 4
while guess != answer and time >= 0:
    if time > 0:
        guess = input('Please enter a number from 1 to 100:')
        if '*' in guess:  # 题目中的额外要求
            print('Sorry,you have entered a wrong format\n')
            continue
        guess = int(guess)
        if guess != answer:
            print('Sorry,you have entered a wrong number')
        elif guess == answer and time == 4:
            print("Jesus Christ!\nYou're so lucky that you found the right number in only one time!"
                  "\nBecause the probability is just 1/100!\nYou definitely meet good things today!")
            break
        else:
            print("Congratulations!You found the right number in " + str(5 - time) + ' times')
            break
        if answer < 10: # 答案是个位数
            if time == 4:
                print("Hint1:It's a single digit\n")
            if time == 3:
                print("Hint2:It's a prime number\n")
            if time == 2:
                print("Now the probability of the number which you will enter is"
                      "\n1/2 or 1/3 or 1/4,so try again\n")  # 这里也可以使用三引号来显示字符
        else:  # 答案是两位数
            if time == 4:
                print("Hint1:It's a double digits.Meanwhile,it's a prime number\n")
            if time == 3:
                print("Hint2:It's tens place is " + str(answer)[0] + "\n")  # 输出答案十位上的数字
            if time == 2:
                print("Now the probability of the number which you will enter is"
                      "\n1 or 1/2 or 1/3 ,so try again\n")
    else:
        print("\nWhat a pity!You didn't find the right number,the answer is " + str(answer))
        break
    time -= 1
