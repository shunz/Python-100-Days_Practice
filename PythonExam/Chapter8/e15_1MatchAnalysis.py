"""体育竞技分析

- 问题的IPO描述
    - 输入：两个球员（A和B）的能力概率，模拟比赛的场次
    - 处理：模拟比赛过程
    - 输出：A和B分别赢得球赛的概率

- 自顶向下设计
    1. 顶层设计
        - 顶层设计是自顶向下设计中最重要的部分
        - 可从问题的IPO描述开始，大多数程序可以将IPO描述直接用到程序结构设计中
            - 本例基础设计的4个步骤（从IPO描述获得，可作为顶层设计）
                1. 打印程序的介绍信息
                    - 针对提升用户体验十分有益
                    - 顶层设计一般不写出具体代码，仅给出函数定义
                    - def main():
                        - printIntro()
                2. 获得程序运行需要的参数（probA、probB、n）
                    - 通过函数将输入语句及输入格式等细节封装或隐藏，只需假设程序如果调用了getInputs()函数即可获取变量的值
                    - def main()
                        - printIntro()
                        - probA, probB, n = getInputs()
                3. 利用球员A和B的能力值probA、probB，模拟n次比赛
                    - 设计一个函数来模拟n场比赛，并返回A和B赢得比赛的结果
                    - def main()
                        - printIntro()
                        - probA, probB, n = getInputs()
                        - winA, winB = simNGames(n, probA, probB)
                4. 输出球员A和B获胜比赛的场次及概率
                    - 设计思路类似，仍然只规划功能和函数
                    - def main()
                        - printIntro()
                        - probA, probB, n = getInputs()
                        - winA, winB = simNGames(n, probA, probB)
                        - printSummary(winsA, winsB)
            - 至此，问题的程序框架已经清晰，但仅是框架，main()函数并没有做什么
            - 原问题被划分为了4个独立的函数，这些函数的名称、输入参数和预期返回值都已确定
        - 这个分解过程十分有益，因为它让程序员在这一步不必关心具体细节而专心考虑程序的结构设计
    2. 第n层设计
        - 每层设计中，参数和返回值如何设计是重点，其他细节可以暂时忽略
        - 确定事件的重要特征而忽略其他细节过程称为「抽象」
        - 抽象是一种基本设计方法，自顶向下的设计过程可看成是发现功能并抽象功能的过程
        - 自顶向下设计的第二阶段是实现或进一步抽象第2层函数
            - printIntro()函数应该输出一个程序介绍，函数由Python基本表达式组合，不增加或改变程序结构
                - def printIntro():
                    - print(‘这个程序模拟两个选手A和B的某种竞技比赛’)
                    - print(‘程序运行需要A和B的能力值（以0到1之间的小数表示）’)
                - getInputs()函数根据提示得到3个需要返回主程序的值
                - simNGames()函数是整个程序的核心
                    - 其基本思路是模拟n场比赛，并跟踪记录每个球员赢得了多少比赛，「模拟n场比赛」直观感受像一个计数循环，而跟踪记录获胜场次更像计数过程。
                    - 这是一个相当直观且粗粒度的设计，类似顶层设计
                    - 其中设计simOneGame()函数，用于模拟一场比赛，需要知道每个球员的概率，返回两个球员的最终得分
                        - 为了模拟一场比赛，需要根据比赛规则来编写代码
                        - 两个球员持续对攻直至比赛结束，可采用无限循环结构直到比赛结束条件成立
                        - 同时需要跟踪记录比赛得分，保留发球局标记
                        - 总之，尽可能详细的模拟比赛过程
                        - 通过随机数和概率确定发球方是否赢得比分（random()<prob），如果球员A发球，那么需要使用A的概率，接着根据发球结果，更新是球员A得分还是将球权交给B
                        - 进一步设计了gameOver()函数，用来表示一场比赛结束的条件，对于不同体育比赛，结束条件可能不同，封装该函数有助于简化根据不同规则修改函数的代价，提高代码可维护性
    3. 设计过程总结
        - 本实例介绍了自顶向下的设计过程
        - 从问题输入输出确定开始，整体设计逐渐向下进行
        - 每一层以大体算法描述开始，然后逐步细化成代码，细节被函数封装
        - 整个过程可以概括为4个步骤
            1. 将算法表达为一系列小问题
            2. 为每个小问题设计接口
            3. 通过将算法表达为接口关联的多个小问题来细化算法
            4. 为每个小问题重复上述过程
        - 自顶向下设计是一种开发复杂程序最具价值的设计理念和工具，设计过程自然且简单，通过封装实现抽象，利用了模块化设计的思想
"""

from random import random

def printIntro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')

def getInputs():
    a = eval(input('请输入选手A的能力值(0-1)：'))
    b = eval(input('请输入选手B的能力值(0-1)：'))
    n = eval(input('模拟比赛的场次：'))
    return a, b, n

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def gameOver(a, b):
    return a == 15 or b == 15

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def printSummary(winsA, winsB):
    n = winsA + winsB
    print(f'竞技分析开始，共模拟{n}场比赛')
    print(f'选手A获胜{winsA}场比赛，占比{winsA/n:.1%}')
    print(f'选手B获胜{winsB}场比赛，占比{winsB/n:.1%}')

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()
    
    
"""result
这个程序模拟两个选手A和B的某种竞技比赛
程序运行需要A和B的能力值（以0到1之间的小数表示）
请输入选手A的能力值(0-1)：0.48
请输入选手B的能力值(0-1)：0.5
模拟比赛的场次：1000
竞技分析开始，共模拟1000场比赛
选手A获胜477场比赛，占比47.7%
选手B获胜523场比赛，占比52.3%
"""
