# Text Progress Bar

'''
要求如下：
(1) 采用sleep()模拟一个持续的进度,获得文本进度条的变化时间；
(2) 通过print()函数实现单行动态刷新，在print()函数中更换参数end的默认值为'',每次使用print()函数输出时不能换行；
(3) 要能回退：打印后光标到之前的位置 \r。
请在Windows的命令行（cmd或PowerShell）或其他操作系统的命令行下执行Python程序，获得进度条效果。
'''

import time
scale = 50

print('执行开始'.center(scale//2,'-'))
start = time.perf_counter()
for i in range(scale+1):
    a = i / scale * 100
    b = '*' * i
    c = '-' * (scale - i)
    dur = time.perf_counter() - start
    print('\r{:3.0f}%[{}->{}]{:.2f}s'.format(a,b,c,dur), end='')
    time.sleep(0.03)

print('\n'+'执行结束'.center(scale//2,'-'))