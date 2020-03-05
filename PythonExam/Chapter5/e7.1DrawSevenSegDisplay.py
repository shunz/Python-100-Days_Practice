"""用七段数码管绘制当前日期

Input：当前日期的数字形式
Process：根据每个数字绘制七段数码管表示
Output：绘制当前日期的七段数码管表示
"""

import turtle as t
import datetime as dt

#t.speed(0)

def drawLine(draw):  # 绘制单段数码管
    t.down() if draw else t.up()
    t.fd(40)
    t.rt(90)

def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(1) if d in [2,3,4,5,6,8,9] else drawLine(0)
    drawLine(1) if d in [0,1,3,4,5,6,7,8,9] else drawLine(0)
    drawLine(1) if d in [0,2,3,5,6,8,9] else drawLine(0)
    drawLine(1) if d in [0,2,6,8] else drawLine(0)
    t.lt(90)
    drawLine(1) if d in [0,4,5,6,8,9] else drawLine(0)
    drawLine(1) if d in [0,2,3,5,6,7,8,9] else drawLine(0)
    drawLine(1) if d in [0,1,2,3,4,7,8,9] else drawLine(0)
    t.lt(180)
    t.up()
    t.fd(20)

def drawDate(date):  # 获得要输出的数字
    for i in date:
        drawDigit(eval(i))

def main():
    t.setup(800, 350, 200, 200)
    t.up()
    t.fd(-240)
    t.pensize(5)
    drawDate(dt.datetime.now().strftime('%Y%m%d'))
    t.ht()

main()
