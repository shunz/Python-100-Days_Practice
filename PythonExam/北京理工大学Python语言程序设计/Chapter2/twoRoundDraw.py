'''
使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。
'''

import turtle as t

# 一共9条边，共2圈，每次左转角度为80度（720/9）
for i in range(9):
    t.fd(100)
    t.left(80)