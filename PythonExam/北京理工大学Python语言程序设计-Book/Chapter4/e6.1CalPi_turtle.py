"""Monte Carlo方法求π值,用turtle绘制呈现

- 求解步骤
    - 随机向单位正方形和圆结构(半径为1)抛洒大量「飞镖」点
    - 计算每个点到圆心的距离，判断该点是否在圆内
    - 用turtle将圆内外的点用两种颜色绘制出来
    - 用圆内的点数除以总点数就是π/4值（圆面积/正方形面积 = πR²/L² = π*1²/2² = π/4）
    - 随机点数量越大，越充分覆盖整个图形，计算得到的π值元精确
    - 实际上，此方法的思想是利用离散点值表示图形的面积，通过面积比例来求解π值
    - 为简化计算，利用图形的1/4求解π值
    - IPO描述
        - 输入
            - 抛点数
        - 处理：
            - 计算每个点到圆心的距离
            - 用turtle绘制点
            - 统计在圆内点的数量
            - 圆内点数 / 总点数 = π/4
        - 输出
            - π值
"""

from random import random
from time import perf_counter, sleep
import turtle

DARTS = 2 ** 13  # 飞镖数
hits = 0  # 命中圆内数
drew = 0  # 已飞数
start = perf_counter()

# init turtle
turtle.setup = (500, 500)
turtle.screensize = (400, 400)
turtle.setworldcoordinates(-20,-20,220,220)
turtle.Screen().delay(0)  # 把画布的延迟取消掉
turtle.Screen().tracer(0)  # 开启/关闭作图过程展示,在绘图之前调用tracer,执行作图代码时，窗口并不会出现任何东西，应该是保持开始作图之前的画面，直到执行turtle.update()刷新画面。应该是就图画在后台内存中画好，然后执行刷新命令时，将内存读取到画面窗口中。

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# draw a square
for _ in range(4):
    t.fd(200)
    t.lt(90)
t.up()

'''    
#生成t2写画点状态信息 (一直闪烁，放弃)
t2 = turtle.Turtle()
t2.hideturtle()
t2.up()
t2.speed(0)
t2.goto(100, -12)
'''

#init()

for i in range(1, DARTS + 1):
    x, y = random(), random()
    dist = (x ** 2 + y ** 2) ** 0.5
    if dist <= 1:
        hits += 1
        # 绘制圆内点
        t.pencolor('tomato')
    else:
        # 绘制圆外点
        t.pencolor('green')

    # 移动&画点
    t.goto(x*200, y*200)
    t.dot()
    drew += 1
    pi = hits / DARTS * 4

    # 输出画点状态
    output = f'{drew}/{DARTS} points, {drew/DARTS:.2%}, \
{perf_counter() - start:.3f}s, Pi ≈ {pi:.7f}'
    turtle.title(output)
    print('\r' + output, end='')
    
    '''
    # 清除之前的t2
    t2.clear()
       
    # 生成新的t2 
    t2 = turtle.Turtle()
    t2.ht()
    t2.up()
    t2.speed(0)
    t2.goto(100, -12)
    t2.write(output, align='center', font=('Arial', 18, 'normal'))
    '''
turtle.Screen().update()  #在绘图结束时调用update
turtle.done()

