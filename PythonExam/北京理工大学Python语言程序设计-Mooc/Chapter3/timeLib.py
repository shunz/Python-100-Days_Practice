import time as t

# 获取当前时间戳（计算及内部时间值，浮点数，从1970-1-1 0:00:00 开始）
# 1567047631.597661
print(t.time())

# 易读的当前时间
# 'Thu Aug 29 11:00:31 2019'
print(t.ctime())

# 获取当前时间，表示为计算机可处理的时间格式
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=29, tm_hour=3, tm_min=4, tm_sec=33, tm_wday=3, tm_yday=241, tm_isdst=0)
print(t.gmtime())

# 时间格式化 strftime = string format?
ti = t.gmtime()
t.strftime('%Y-%m-%d %H:%M:%S', ti)
timeStr = '2018-01-26 12:55:20'
t.strptime(timeStr, '%Y-%m-%d %H:%M:%S')

# 测量时间：perf_counter()
# 产生时间：sleep()
start = t.perf_counter()
t.sleep(1)
end = t.perf_counter()
print(end-start)

def wait():
    t.sleep(3)
    print('Tada~~~, 3 sec is passed.')

wait()