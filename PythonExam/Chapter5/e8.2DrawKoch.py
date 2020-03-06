"""科赫雪花绘制"""

import turtle as t

def koch(size, n):  # size:线条长度，n:阶数
    if n == 0:  # 递归基例
        t.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            t.lt(angle)
            koch(size/3, n-1)

def main():
    t.setup(600, 600)
    t.speed(0)
    t.shape('turtle')
    t.pencolor('tomato')
    t.up()
    t.goto(-200, 120)
    t.down()
    t.pensize(2)
    for _ in range(3):
        koch(400, 4)
        t.rt(120)
    t.ht()

main()
