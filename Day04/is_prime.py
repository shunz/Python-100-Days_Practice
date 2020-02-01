'''
练习1：输入一个正整数判断是不是素数
提示：素数指的是只能被1和自身整除的大于1的整数

Version: 0.1
Author: Shunz
Last update: 2020-01-10
'''

from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d 是素数' % num)
else:
    print('%d 不是素数' % num)
    for i in range(2, num):
        if num % i == 0:
            print('%d 能被 %d 整除'%(num, i))
