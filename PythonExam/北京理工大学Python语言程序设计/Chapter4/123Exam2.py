# 100 以内素数之和
import time as t

sum = 0
num = []
start = t.perf_counter()
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            print('{} 等于 {} * {}'.format(i,j,i//j))
            break
    else:
        print('{} 是素数'.format(i))
        num.append(i)
        sum += i
elapsed = t.perf_counter() - start
print('计算耗时：{:.3f} 秒'.format(elapsed))
print('100 以内素数有：{}'.format(num))
print('100 以内素数之和：{}'.format(sum))

