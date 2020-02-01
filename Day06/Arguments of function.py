'''
函数的参数
'''

from random import randint

def roll_dice(n = 2):
    '''摇色子'''
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add1(a = 0, b = 0, c = 0):
    '''三个数相加'''
    return a + b + c

# 未指定参数使用默认值摇两颗色子
print(roll_dice())

# 摇三颗色子
print(roll_dice(3))

# 不同数量参数相加
print(add1())
print(add1(1))
print(add1(1,2))
print(add1(1,2,3))

# 传递参数可以不按设定顺序进行传递
print(add1(c=50, a=100, b= 300))

# 参数名前的*表示其是一个可变参数
def add2(*args):
    # Python函数可以返回多个值，以元组方式返回
    return args, sum(args)

# 在调用时可传入任意个参数
print(add2())
print(add2(1,2,3))

