"""5.10

请利用datetime库将当前系统时间转换为字符串
"""
from datetime import datetime
print('现在是{0:%Y}年{0:%m}月{0:%d}日，{0:%A}，{0:%I}:{0:%M}:{0:%S} {0:%p}'.format(datetime.now()))


# 5.11
print('美式日期格式：{0:%I}:{0:%M}{0:%p} {0:%b}/{0:%d}/{0:%Y}'.format(datetime.now()))
print('英式日期格式：{0:%I}:{0:%M}{0:%p} {0:%d}-{0:%m}-{0:%Y}'.format(datetime.now()))


# 5.12
# datetime对象可以直接做加减法，可以用来给程序计时
from time import perf_counter

start = datetime.now()
start2 = perf_counter()
'''
要计时的代码
'''
counts = 2**19
for i in range(counts):
    print('\r' + f'{i/counts:.2%}, 用time.perf_counter()计时:{perf_counter() - start2:.5f}s', end='')
end = datetime.now()
interval = end - start

print()
print(interval)
print(type(interval))  # <class 'datetime.timedelta'>
print(f'用datatime.now()计时：{interval.seconds + interval.microseconds/1000000:.5f}s')
