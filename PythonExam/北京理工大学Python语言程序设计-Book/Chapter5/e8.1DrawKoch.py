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
    t.setup(800,400)
    t.speed(0)
    t.up()
    t.goto(-300, -50)
    t.down()
    t.pensize(2)
    koch(600, 3)
    t.ht()

main()
