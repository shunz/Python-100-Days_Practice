'''
找出10000以内的完美数

完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
'''


'''
lists = []
for i in range(1, 10001):
    # 找出i的所有真因子，放入一个列表
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            lists.append(j)
    # 判断所有真因子之和是否等于i
    if i == sum(lists):
        print(i, end = ' ')
'''

'''
for num in range(1, 10000):
    result = 0
    for factor in range(1, int(num ** 0.5) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num //factor
        if result == num:
            print(num)
'''
import math
for n in range(1, 10000):
    # 找出n的所有真因子，放入一个列表
    lists = []
    for f in range(1, n):
        if n % f == 0:
            lists.append(f)
    # 判断所有真因子之和是否等于n
    if sum(lists) == n:
        print(n, lists)
