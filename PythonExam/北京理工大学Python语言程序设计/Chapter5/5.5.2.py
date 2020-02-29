# 科赫雪花绘制小包裹 KochDrawV1.py

import turtle

def koch(size, n): #线段长度，阶数
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
        #for angle in [0, 90, -90, -90, 90]: # 绘制正方形转折线
            turtle.left(angle)
            koch(size/3, n-1)

# def main(): # 绘制单条科赫曲线
#     turtle.setup(800, 400)
#     turtle.penup()
#     turtle.goto(-300, -50)
#     turtle.pendown()
#     turtle.pensize(2)
#     koch(600, 4)
#     turtle.hideturtle()

def main(level): # 绘制科赫雪花
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()

main(3)

# Pyinstaller 打包命令行参数
# pyinstaller --windowed --onefile --clean --noconfirm -F 5.5.2.py
