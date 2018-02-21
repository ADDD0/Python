temp = 'ii3l01oO8vu5e[gp+zy]9t,rhJLo6onnn'  # Program 1 破译字符串
print(temp[::3])  # 最简版
print(temp[0:32:3])  # 完整版
print('')
# Program 2 密码安全性检查代码
#
# 低级密码(Low-level)要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度不大于8位
#
# 中级密码(Medium-level)要求:
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不低于8位且不大于10位
#
# 高级密码(High-level)要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不低于10位
#
#   未满足要求时按所得分数评定：
#   低级密码得分：0~50
#   中级密码得分：51~75
#   高级密码得分：76~100
special_characters = '~!@#$%^&*()_=-/,.?<>;:[]{}\|'
number_amount = '0,1,2,3,4,5,6,7,8,9'


def judgement(temp_):
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for i in temp_:
        if i.isalpha():
            temp1 += 1
        else:
            continue
    for i in temp_:
        if i.isnumeric():
            temp2 += 1
        else:
            continue
    for i in temp_:
        if i in special_characters:
            temp3 += 1
        else:
            continue
    temp1 = str(temp1)
    temp2 = str(temp2)
    temp3 = str(temp3)
    return[temp1, temp2, temp3]


password = input('Please enter your password:')
temp4 = judgement(password)
while temp4.count('0') == 3:
    password = input("Sorry,you have entered a wrong format.Please try another password:")
    temp4 = judgement(password)
if temp4[1] != '0' and temp4[0] == '0' and len(password) <= 8:
    print("'" + password + "' is a Low-level password.")
if temp4[1] == '0' and temp4[0] != '0' and len(password) <= 8:
    print("'" + password + "' is a Low-level password.")
elif temp4.count('0') == 1 and 8 <= len(password) <= 10:
    print("'" + password + "' is a Medium-level password.")
elif temp4.count('0') == 0 and password[0].isalpha() and len(password) >= 10:
    print("'" + password + "' is a High-level password.")
else:
    alpha, number, special_character = str(temp4[0]), int(temp4[1]), int(temp4[2])
    temp5 = len(password)
    score1 = 5 if temp5 < 8 else 10 if 8 <= temp5 <= 10 else 25
# 一、长度（25分）
# 5分:小于8个字符
# 10分:8到10个字符
# 25分:大于10个字符
    score2 = 0 if password.isalpha() else 10 if alpha.isupper() or alpha.islower() else 25
# 二、字母组成（25分）
# 0分:没有字母
# 10分:全都是小（大）写字母
# 25分:大小写混合字母
    score3 = 0 if password.isdigit() else 10 if number <= 2 else 20
# 三、数字组成（20分）
# 0分:没有数字
# 10分:1或2个数字
# 20分:大于2个数字
    score4 = 0 if special_character == 0 else 10 if special_character == 1 else 25
# 四、其它特殊符号（25分）
# 0分:没有符号
# 10分:1个符号
# 25分:大于1个符号
    score_additional = 0               # 五、额外奖励（5分）
    if int(alpha) > 0 and number > 0:  # 2分:字母和数字
        score_additional = 2           # 3分:字母、数字和符号
        if special_character > 0:      # 5分:大小写字母、数字和符号
            score_additional = 3
            if score2 == 25:
                score_additional = 5
    final_score = score1 + score2 + score3 + score4 + score_additional
    if final_score <= 50:
            print("It's final score is " + str(final_score) + '.So "' + password + '" is a Low-level password.')
    if 50 < final_score <= 75:
            print("It's final score is " + str(final_score) + '.So "' + password + '" is a Medium-level password.')
    if 75 < final_score <= 100:
            print("It's final score is " + str(final_score) + '.So "' + password + '" is a High-level password.')
print("""You can improve your password's level by:
    1. Increase the length.
    2. Add more alphabets and numbers.
    3. Add some uppercase letters or lowercase letters.
    4. Add some special characters like '~!@#$%^&*()_=-/,.?<>;:[]{}\|'.""")
print('\nThe End')
