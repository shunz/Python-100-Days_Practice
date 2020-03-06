"""实现multi()函数

参数个数不限，返回所有参数的乘积
"""

def multi(*args):
    sum = 1
    count = 1
    for i in args:
        if type(i) is type(1) or type(i) is type(1.):
            sum *= i
        else:
            print(f'第{count}项不是一个有效的整数！')
            return
        count += 1
    return sum

print(multi(2,3,1.0,5,4.99))
print(multi(2.1, 'str'))
print(multi())
