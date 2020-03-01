"""Monte Carlo方法求π值

- 求解步骤
    - 随机向单位正方形和圆结构(半径为1)抛洒大量「飞镖」点
    - 计算每个点到圆心的距离，判断该点是否在圆内
    - 用圆内的点数除以总点数就是π/4值（圆面积/正方形面积 = πR²/L² = π*1²/2² = π/4）
    - 随机点数量越大，越充分覆盖整个图形，计算得到的π值元精确
    - 实际上，此方法的思想是利用离散点值表示图形的面积，通过面积比例来求解π值
    - 为简化计算，利用图形的1/4求解π值
    - IPO描述
        - 输入
            - 抛点数
        - 处理：
            - 计算每个点到圆心的距离
            - 统计在圆内点的数量
            - 圆内点数 / 总点数 = π/4
        - 输出
            - π值
"""

from random import random
from time import perf_counter

DARTS = 2 ** 24
hits = 0
start = perf_counter()
for i in range(1, DARTS + 1):
    x, y = random(), random()
    dist = (x ** 2 + y ** 2) ** 0.5
    if dist <= 1:
        hits += 1
pi = hits / DARTS * 4
print(f'Pi值是{pi}')
print(f'运行时间：{perf_counter() - start:.3f}s')
