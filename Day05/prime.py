'''
输出100以内的所有素数

素数指的是只能被1和自身整除的正整数(不包括1)
'''

count = 0
ranges = 200
for n in range(1, ranges):
    for f in range(2, n):
        if n % f == 0:
            break
    else:
        print(n, end=' ')
        count += 1


print('\n%d以内的素数一共%d个' % (ranges, count))
