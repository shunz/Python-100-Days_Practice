'''
猜数字游戏
电脑出一个1~100之间的随机整数，由人来猜
电脑根据人猜的数字分别给出提示大一点/小一点/猜对了

Version: 0.1
Author: Shunz
Last_Update: 2020-01-10
'''

from random import randint as ri

answer = ri(1, 100)
count = 0

while True:
    count += 1
    num = int(input('请输入：'))
    if num > answer:
        print('小一点')
    elif num < answer:
        print('大一点')
    else:
        print('猜对了')
        break

print('你共猜了 %d 次' % count)
if count > 7:
    print('你的智商余额不足 ^__^')

    
