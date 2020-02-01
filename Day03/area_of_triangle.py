'''
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: Shunz
Date: 2020-01-09
'''

# import math
from math import sqrt as sr

def area_of_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print('周长：%.2f' % (perimeter))
        # sp is short for semi perimeter
        sp = perimeter / 2
        area = sr(sp * (sp - a) * (sp - b) * (sp - c))
        print('面积：%.2f' % (area))
    else:
        print('边长参数无法构成三角形')

area_of_triangle(33, 44, 55)
