"""车羊门问题

有3扇关闭的门，一扇门后停着车，其余是山羊，只有主持人知道门后是什么。参赛者可以选择一扇门，在开启它之前，
主持人会开启另外一扇门，露出门后的山羊，然后允许参赛者更换自己的选择。
请问：参赛者更换选择后能否增加猜中汽车的机会？ ———— 这是一个经典问题。
请使用random库对这歌随机事件进行预测，分别输出参赛者改变选择和坚持选择获胜的几率
"""

import random as r
import time as t

times = 2 ** 20 # eval(input('请输入你希望模拟的次数：'))

insist = 0
change = 0
start = t.perf_counter()

for i in range(1, times+1):
    car = r.randint(0, 2)  # 生成哪个门后藏车
    choice = r.randint(0, 2)  # 随机初选
    if choice == car:  # 如果直接选中，则初选正确，即坚持选择就能中
        insist += 1
    else:  # 如果初选不中，则主持人打开另一扇门后，改选就能中
        change += 1
    print('\r' + f'坚持初选_胜率{insist/times:.2%}; 改变初选_胜率{change/times:.2%}, \
{i}/{times}, {t.perf_counter() - start:.2f}s', end='')

