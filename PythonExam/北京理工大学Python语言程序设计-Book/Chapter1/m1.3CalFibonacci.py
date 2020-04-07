"""微实例1.3 斐波那契数列的计算"""

a, b = 0, 1
n = 0
while n < 64:
    a, b = b, a + b
    n += 1
    print(a, end=',')
