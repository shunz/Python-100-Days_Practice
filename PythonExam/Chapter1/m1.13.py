"""1.13 五角星的绘制

绘制一个红色的五角星图形

Input: 内部参数
Process: 调用turtle库绘制五角星的各条线
Output: 绘制五角星
"""

from turtle import *

fillcolor('red')
begin_fill()
for _ in range(5):
    fd(200)
    rt(144)
end_fill()
done()

'''
while True:
    fd(200)
    rt(144)
    if abs(pos()) < 1:
        break
'''
