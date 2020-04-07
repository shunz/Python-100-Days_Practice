# 实例6：圆周率的计算
# 求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，根据在1/4圆内点的数量占总撒点数的比例计算圆周率值。
# 以123作为随机数种子，获得用户输入的撒点数量，编写程序输出圆周率的值，保留小数点后6位。

import random as r
# from random import random, seed

darts = eval(input())
hits = 0
r.seed(123)

for i in range(1,darts+1):
    x,y = r.random(),r.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        hits += 1

pi = hits / darts * 4
print('{:.6f}'.format(pi))
