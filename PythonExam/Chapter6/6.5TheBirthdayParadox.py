"""生日悖论分析

生日悖论指的是如果一个房间里有23人或以上，那么至少有两个人生日相同的概率大于50%。
编写程序，输出在不同随机样本数量下，23个人中至少两个人生日相同的概率

- 输入
    - n个人
    - s次随机样本量
- 处理
    - 随机生成n个人的生日
    - 判断其中是否有重复
    - 随机生成&判断s次
    - 累加重复数/随机样本量s = 生日相同的概率
- 输出
    - s次随机样本数量下，n个人中至少两个人生日相同的概率
"""

from random import *

def randbirth():
    month = randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month == 2:
        day = randint(1, 28)
    else:
        day = randint(1, 30)
    return month * 100 + day

def isSame(num):
    ls = []
    for i in range(num):
        ls.append(randbirth())
    if len(ls) == len(set(ls)):
        return 0
    else:
        return 1

def main():
    try:
        probability = 0
        n, s = eval(input('请输入人数和样本数量(如:23,1000)：'))
        for i in range(s):
            if isSame(n) == 1:
                probability += 1
        print(f'随机样本数量为{s}时，房间里{n}个人中至少两人生日相同的概率是{probability / s:.2%}')
    except:
        print('输入有误')
            
main()
