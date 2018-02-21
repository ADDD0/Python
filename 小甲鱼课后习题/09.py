import random
prime_number = [2, 3, 5, 7]  # Program 1 猜密码（猜数字升级版）
number = 0
for i in range(2, 100):
    if i % 2 and i % 3 and i % 5 and i % 7 != 0:
        prime_number.append(i)
        number += 1
    else:
        continue
answer = prime_number[random.randint(0, number+4)]
guess = 1
time = 4
while guess != answer and time >= 0:
    if time > 0:
        guess = input('Please enter a number from 1 to 100:')
        if '*' in guess:
            print('Sorry,you have entered a wrong format.\n')
            continue
        guess = int(guess)
        if guess != answer:
            print('Sorry,you have entered a wrong number.')
        elif guess == answer and time == 4:
            print("Jesus Christ!\nYou're so lucky that you found the right number in only one time!"
                  "\nBecause the probability is just 1/25!\nYou definitely meet good things today.")
            break
        else:
            print("Congratulations!You found the right number in "+str(5-time)+' times.')
            break
        if 0 < answer < 10:
            if time == 4:
                print("Hint1:It's a single digit.\n")
            if time == 3:
                print("Hint2:It's a prime number.\n")
            if time == 2:
                print("Now the probability of the number which you will enter is"
                      "\n1/2 or 1/3 or 1/4,so try again.\n")
        elif answer > 10:
            if time == 4:
                print("Hint1:It's a double digits.Meanwhile,it's a prime number.\n")
            if time == 3:
                print("Hint2:It's tens place is "+str(answer)[0]+" .\n")
            if time == 2:
                print("Now the probability of the number which you will enter is"
                      "\n1 or 1/2 or 1/3 ,so try again.\n")
    else:
        print("\nWhat a pity!You didn't find the right number,the answer is " + str(answer) + ' .')
        break
    time -= 1
print('')
for i in range(100, 1000):  # Program 2.1 求水仙花数(最简便？)
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        print(i, end=' ')
print('\n')
total = 0  # Program 2.2 运用本节课知识
for i in range(100, 1000):
    temp = i
    while temp:
        total = total + (temp % 10)**3
        temp //= 10
    if sum == i:
        print(i, end=' ')
print('\n')
for red in range(1, 4):  # Program 3 练习题
    for yellow in range(1, 4):
        for green in range(2, 7):
            if red+yellow+green == 8:
                print('red\t'*red+'yellow\t'*yellow+'green\t'*green)
print('\nThe End')
