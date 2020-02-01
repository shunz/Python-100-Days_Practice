'''
判断输入的正整数是不是回文数

回文数是指将一个正整数从左往右排列和从右往左排列值都是一样的数

'''


for n in range(10000):
    temp = n
    n2 = 0
    while temp > 0:
        n2 *= 10
        n2 += temp % 10
        temp //= 10
    if n == n2:
        print(n)
