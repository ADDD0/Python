# 游戏编程:按以下要求定义一个乌龟类和鱼类并尝试编写游戏
# 游戏场景范围(0,0)~(10,10)
# 生成1只乌龟和10条鱼
# 移动方向均随机
# 乌龟移动能力1或2,鱼移动能力1
# 移动到场景边缘,反向移动
# 乌龟初始化体力为100(上限)且每移动一次消耗1
# 坐标重叠时鱼被吃掉,乌龟体力值+20
# 乌龟体力为0时或鱼数目为0时游戏结束
import random as r

legal_x = [0, 10]
legal_y = [0, 10]


class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置
        nextstep = r.choice([[0, 0], [0, 1], [0, 2], [0, -1],
                             [0, -2], [1, 0], [2, 0], [-1, 0], [-2, 0]])
        [new_x, new_y] = [self.x + nextstep[0], self.y + nextstep[1]]
        # 检查移动后是否超出x轴边界
        if new_x < legal_x[0]:
            self.x = 2 * legal_x[0] - new_x
        if new_x > legal_x[1]:
            self.x = 2 * legal_x[1] - new_x
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < legal_y[0]:
            self.y = 2 * legal_y[0] - new_y
        if new_y > legal_y[1]:
            self.y = 2 * legal_y[1] - new_y
        else:
            self.y = new_y
        # 体力消耗
        if nextstep != [0, 0]:
            self.power -= 1
        # 返回移动后的新位置
        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])

    def move(self):
        # 随机计算方向并移动到新的位置
        nextstep = r.choice([[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]])
        [new_x, new_y] = [self.x + nextstep[0], self.y + nextstep[1]]
        # 检查移动后是否超出x轴边界
        if new_x < legal_x[0]:
            self.x = 2 * legal_x[0] - new_x
        elif new_x > legal_x[1]:
            self.x = 2 * legal_x[1] - new_x
        else:
            self.x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < legal_y[0]:
            self.y = 2 * legal_y[0] - new_y
        elif new_y > legal_y[1]:
            self.y = 2 * legal_y[1] - new_y
        else:
            self.y = new_y
        # 返回移动后的新位置
        return self.x, self.y


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while 1:
    if not len(fish):
        print('The fish were all eaten\nGame over')
        break
    if not turtle.power:
        print('Turtle exhausted\nGame over')
        break

    pos = turtle.move()
    for each_fish in fish:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print('A fish was eaten at {0}'.format(pos))
