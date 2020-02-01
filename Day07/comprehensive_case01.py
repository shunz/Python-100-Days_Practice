'''
综合案例1：双色球选号
'''

from random import randrange, randint, sample

def random_select():
    '''
    随机选择一组号码
    '''
    selected_balls = []
    # 从红球号码1~33中随机取6个不重复的号码
    # red_balls = [x for x in range(1, 34)]
    selected_balls = sample(range(1, 34), 6)
    selected_balls.sort()
    # 从蓝球号码1~15从随机取1个
    selected_balls.append(randint(1, 16))
    return selected_balls

def display(balls):
    '''
    输出列表中的双色球号码
    '''
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end = ' ')
        # print('%02d' % ball, end = ' ')
        print(f'{ball:02}', end = ' ')
    print()

if __name__ == '__main__':
    while True:
        n = int(input('机选几注：'))
        for _ in range(n):
            display(random_select())
