'''
掷骰子决定做什么事情

Version: 0.1
Author: Shunz
Date: 2020-01-09
'''

from random import randint

def rolldice():
    face = randint(1,6)
    if face == 1:
    	result = '唱首歌'
    elif face == 2:
    	result = '跳个舞'
    elif face == 3:
    	result = '学狗叫'
    elif face == 4:
    	result = '做俯卧撑'
    elif face == 5:
    	result = '念绕口令'
    elif face == 6:
    	result = '讲冷笑话'
    print(result)


for i in range(20):
    rolldice()
