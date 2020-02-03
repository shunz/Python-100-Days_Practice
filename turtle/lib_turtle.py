'''
turtle ——— 海龟绘图
https://docs.python.org/zh-cn/3/library/turtle.html

源自1967年创造的Logo编程语言
很适合引导孩子学习编程

'''

from turtle import *


# Turtle方法

## 海龟动作

### 移动和绘制
'''
- forward() | fd() 前进
- backward() | bk() | back() 后退
- right() | rt() 右转
- goto() | setpos() | setposition() 前往/定位
- setx() 设置x坐标
- sety() 设置y坐标
- setheading() | seth() 设置朝向 (0-东|90-北|180-西|270-南)
- home() 返回原点
- circle() 画圆
- dot() 画点
- stamp() 印章
- clearstamp() 清除印章
- clearstamps() 清除多个印章
- undo() 撤销
- speed()
'''
speed('fast')

print(position())
fd(25)
print(pos())
fd(-75)
print(pos())

bk(30)
print(pos())

print(heading())
rt(45)
lt(90)
print(heading())

tp = pos()
print(tp)
goto(60,30) # 移至一个绝对坐标，画笔落下时将画线，不改变朝向
setpos(20, 50)
setposition(100, 200)

setx(-50)
sety(30)

seth(0)
setheading(90)
print(heading())

home() # 移至初始坐标，设置朝向为初始方向
print(heading())
print(position())

'''
circle(半径, [夹角], [边数])
- 圆心在海龟左边
- 海龟的朝向会随夹角参数改变
- 圆实际是以其内切正多边形近似表示，边数参数可以用来绘制正多边形
'''
reset()
speed(6)
circle(50)
circle(80, 180)
circle(100, 360, 5)

dot() # 绘制直径为size的圆点，若未指定，取pensize+4和2*pensize中的较大值
dot(5,'blue') # 可指定颜色

fd(30)
color('red')
stp_id = stamp() # 在当前位置印制一个海龟形状，返回stamp_id，可通过clearstamp(stamp_id)删除
fd(30)
clearstamp(stp_id)

for _ in range(6):
    stamp(); fd(30)

clearstamps(2) # 删除前2个印章
clearstamps(-2) # 删除后2个印章
clearstamps() # 删除所有印章

for _ in range(6):
    undo() # 撤销最近的动作，可撤销次数由缓冲区大小决定

'''
Speed参数默认为None，可设0..10整数或速度字符串
- 'fastest': 0 最快，没有动画效果(直接跳至或转向至目标位置或朝向)
- 'fast': 10 快
- 'normal': 6 正常
- 'slow': 3 慢
- 'slowest': 1 最慢
'''
speed('normal')
speed(9)
print(speed())



### 获取海龟的状态
'''
- position() | pos() 位置
- towards() 目标方向
- xcor() x坐标
- ycor() y坐标
- heading 朝向
- distance() 距离
'''
print(position())
print(pos())

print(towards(0, 0)) # 从海龟位置到(x, y)连线的夹角，依赖于初始朝向

print(xcor()) # 海龟的 x 坐标
print(ycor()) # 海龟的 y 坐标

print(heading()) # 海龟的朝向

print(distance(0, 0)) # 从海龟位置到(x, y)之间的距离



### 设置与度量单位
'''
degrees() 角度
radians() 弧度
'''
degrees(400.0) # 设置角度的度量单位，默认为360
seth(100.0)
degrees(360)
print(heading()) # 90.0

radians() # 设置角度的度量单位为弧度。其值等于 degrees(2*math.pi)
heading() # 1.5707......
degrees(360)



## 画笔状态

### 绘图状态
'''
- pendown() | pd() | down() 画笔落下
- penup() | pu() | up() 画笔抬起
- pensize() | width() 画笔粗细
- pen() 返回或设置画笔属性
- isdown() 画笔是否落下
'''
pensize() # 返回当前线条大小
pensize(2)

'''
画笔属性，是一个包含以下键值对的「画笔字典」
此字典可作为后续调用pen()时的参数，以恢复之前的画笔状态
- 'shown': True/False
- 'pendown': True/False
- 'pencolor': 颜色字符串或颜色元组
- 'fillcolor': 颜色字符串或颜色元组
- 'pensize': 正数值
- 'speed': 0..10 范围内的数值
- 'resizemode': 'auto'、'user'、'noresize'
- 'stretchfactor': (正数值, 正数值)
- 'outline': 正数值
- 'tilt': 数值
'''
pen() # 返回画笔属性，包含以上键值对的「画笔字典」
pen(fillcolor='red', pencolor='green', pensize=3)
sorted(pen().items())
penstate = pen()
color('purple','')
penup()
sorted(pen().items())[:3]
pen(penstate, fillcolor='brown')
sorted(pen().items())[:3]

isdown() # 若画笔落下返回 True



### 颜色控制
'''
- color() 颜色
- pencolor(*args) 画笔颜色
- fillcolor(*args) 填充颜色
'''
pencolor() # 返回画笔颜色，可用作其他color调用的输入
pencolor('#33cc99') # 设置画笔颜色，>>> (0.2, 0.8, 0.6)
pencolor('red')

colormode(255) # 设置颜色模式为255
pencolor((255,255,255)) # 设置画笔颜色为以r,g,b元组表示的RGB颜色
pencolor(128,128,128)

colormode(1) # 设置颜色模式为1
pencolor((1,1,1))
pencolor(0.5,0.5,0.5)
tup = (0.2, 0.8, 0.55)
pencolor(tup)

color() # 以元组返回一对颜色字符串或颜色元组表示当前画笔颜色和填充色
color('pink', 'blue')
color('#285078', '#234568')
colormode(1)
color(0.2, 0.4, 0.6)
colormode(255)
color(80, 160, 240)



### 填充
'''
- filling() 是否填充
- begin_fill() 开始填充
- end_fill() 结束填充
'''
begin_fill() # 在绘制要填充的形状之前调用
if filling():
    fillcolor('yellow')
    circle(80)
end_fill() # 填充上次调用 begin_fill() 之后绘制的形状



### 更多绘图控制
'''
- reset() 重置
- clear() 清空
- write() 书写
'''
reset() # 从屏幕中删除海龟的绘图，海龟回到原点并设置所有变量为默认值
clear() # 从屏幕中删除指定海龟的绘图，不移动海龟; 海龟的状态、位置以及其他海龟的绘图不受影响

'''
write(arg, move=False, align='left', font=('Arial, 8, 'normal'))
- arg: 要书写到 TurtleScreen 的对象，指定的字符串到当前海龟位置
- move: True/False, 为True时，画笔移动到文本的右下角
- align: 'left', 'center', 'right'
- font: 一个三元组(fontname, fontsize, fonttype)
'''
write('Home=', True, align='center')
write((0,0), True)



## 海龟状态

### 可见性
'''
- showturtle() | st() 显示海龟
- hideturtle() | ht() 隐藏海龟
- isvisible() 是否可见
'''
showturtle()
hideturtle()
ht()
st()
print(isvisible())



### 外观
'''
- shape() 形状
- resizemode() 大小调整模式
- shapesize() | turtlesize() 形状大小
- shearfactor() 剪切因子
- settiltangle() 设置倾角
- tiltangle() 倾角
- tilt() 倾斜
- shapetransform() 变形
- get_shapepoly() 获取形状多边形
'''
shape() # 返回当前的形状名
shape('turtle') # 指定形状名(arrow,turtle,circle,square,triangel,classic)

resizemode() # 返回当前大小调整模式
resizemode('auto') # 根据画笔粗细值调整海龟的外观
resizemode('user') # 根据拉伸因子和轮廓宽度(outline)值调整海龟的外观，两者是由 shapezise() 设置的
resizemode('noresize') # 不调整海龟的外观大小

'''
shapesize(stretch_wid, stretch_len, outline)
返回或设置画笔的属性 x/y-拉伸因子和/或轮廓，需配合resizemode('user')
- stretch_wid: 垂直于其朝向的宽度拉伸因子
- stretch_len: 平等于其朝向的长度拉伸因子
- outline: 轮廓宽度
'''
shapesize()
resizemode('user')
shapesize(5, 5, 20)
shapesize(outline=8)

shearfactor() # 返回当前剪切因子(剪切角度的切线)
shearfactor(0.5) # 设置剪切因子

reset()
shape('turtle')
tilt(30) # 海龟形状当前倾角转动指定角度，不改变海龟的朝向(移动方向)

settiltangle(45) # 旋转海龟形状，忽略倾角，不改变朝向

tiltangle() # 返回或指定当前的倾角
tiltangle(60)

shapetransform() # 返回或设置海龟形状的当前变形矩阵

get_shapepoly() # 返回以坐标值对元组表示的当前形状多边形，可用于定义一个新形状或一个复合形状的多个组成部分



## 使用事件
'''
- onclick() 当鼠标点击
- onrelease() 当鼠标释放
- ondrag() 当鼠标拖动
'''



## 特殊海龟方法
'''
- begin_poly() 开始记录多边形
- end_poly() 结束记录多边形
- get_poly() 获取多边形
- clone() 克隆
- getturtle() | getpen() 获取海龟画笔
- getscreen() 获取屏幕
- setundobuffer() 设置撤销缓冲区
- undobufferentries() 撤销缓冲区条目数
'''



# TurtleScreen / Screen 方法

## 窗口控制
'''
- bgcolor() 背景颜色
- bgpic() 背景图片
- clear() | clearscreen() 清屏
- reset() | resetscreen() 重置
- screensize() 屏幕大小
- setworldcoordinates() 设置世界坐标系
'''



## 动画控制
'''
- delay() 延迟
- tracer() 追踪
- update() 更新
'''



## 使用屏幕事件
'''
- listen() 监听
- onkey() | onkeyrelease() 当键盘按下并释放
- onkeypress() 当键盘按下
- onclick() | onscreenclick() 当点击屏幕
- ontimer() 当达到定时
- mainloop | done() 主循环
'''



## 设置与特殊方法
'''
- mode() 模式
- colormode() 颜色模式
- getcanvas() 获取画布
- getshapes() 获取形状
- register_shape() | addshape() 添加形状
- turtles() 所有海龟
- window_height() 窗口高度
- window_width() 窗口宽度
'''


## 输入方法
'''
- textinput() 文本输入
- numinput() 数字输入
'''



## Screen 专有方法
'''
- bye() 退出
- exitonclick() 当点击时退出
- setup() 设置
- title() 标题
'''




'''
# Draw a shape
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
