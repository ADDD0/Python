# 导入模块方法
# 第一种:import 模块名
# 第二种:from 模块名 import 函数名(也可以使用通配符*)
# 第三种:import 模块名 as 新名字
import TemperatureConversion as tc

print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))
