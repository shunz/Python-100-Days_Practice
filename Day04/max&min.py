'''
练习2：输入两个正整数，计算他们的最大公约数和最小公倍数

Ver: 0.1
Author: Shunz
Last_update: 2020-01-10
'''

x = int(input('x= '))
y = int(input('y= '))

# 如果x大于y就互换其值
if x > y:
    x, y = y, x

# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d 和 %d 的最大公约数是 %d'%(x, y, factor))
        print('%d 和 %d 的最小公倍数是 %d'%(x, y, x * y // factor))
        break
