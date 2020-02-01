'''
练习1：实现计算求最大公约数和最小公倍数的函数
'''

def gys(x, y):
    '''求最大公约数'''
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def gbs(x, y):
    '''求最小公倍数'''
    return(x * y // gys(x, y))

if __name__ == '__main__':
    while True:
        # x = 120
        # y = 25
        x = int(input('x = '))
        y = int(input('y = '))
        print('%d和%d的最大公约数是%d' % (x, y, gys(x, y)))
        print('%d和%d的最小公倍数是%d' % (x, y, gbs(x, y)))
