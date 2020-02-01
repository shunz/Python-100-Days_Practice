'''
综合案例2：约瑟夫环问题

《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
'''

def main():
    # 列出30个人，每个人都标为True
    persons = [True] * 30
    # counter: 数出15个扔到海里的人
    # index: 人在30个人组成的列表里的下标数
    # number: 报数值
    counter, index, number = 0, 0, 0
    # 循环直到数出15个人为止
    while counter < 15:
        # 只有为True的人才参与报数
        if persons[index]:
            # 报数+1
            number += 1
            if number == 9:
                # 数到9的人标为False
                persons[index] = False
                # 仍海人数+1
                counter += 1
                # 报数值清零
                number = 0
        # 下标数+1
        index += 1
        # ？？？
        index %= 30
    # 遍历人员列表，标True的显示「基」，否则显示「非」
    for person in persons:
        print('活' if person else '死', end=' ')

if __name__ == '__main__':
    main()
