# 蒙特卡罗求解圆周率方法
# CalpiV2.py

from random import random
from time import perf_counter

darts = 1000 ** 2
hits = 0
start = perf_counter()

for i in range(1,darts+1):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/darts)
print('圆周率值是：{}'.format(pi))
print('运行时间是：{}'.format(perf_counter() - start))
