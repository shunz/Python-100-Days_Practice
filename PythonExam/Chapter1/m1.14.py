"""1.14 太阳花的绘制

绘制一个太阳花的图形

Input: 内部参数
Process: 调用turtle库绘制太阳花的各条线
Output: 绘制太阳花
"""

from turtle import *

speed(10)
color('tomato', 'seashell')
begin_fill()
while True:
    fd(200)
    lt(175)
    if abs(pos()) < 1:
        break
end_fill()
done()
