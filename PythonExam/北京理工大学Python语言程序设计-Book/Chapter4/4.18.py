from random import *
# 随机生成100内的10个整数
print([randint(0, 100) for _ in range(10)])
print(sample(range(100), 10))


# 随机选取0到100内的奇数
print(randrange(1, 100, 2))
print(choice([i for i in range(100) if i % 2 == 1]))
print(sample([i for i in range(100) if i % 2 == 1], 1).pop())


# 从字符串'abcdefghij'中随机选取4个字符
ls = 'abcdefghij'
print(sample([i for i in ls] ,4))
print([choice([i for i in ls]) for _ in range(4)])
print([ls[randint(0, len(ls)-1)] for _ in range(4)])


# 随机选取列表['apple','pear','peach','orange']中的1个字符串
ls2 = ['apple','pear','peach','orange']
print(choice(ls2))
print(ls2[choice(range(4))])
print(ls2[randint(0,3)])
print(ls2[randrange(0,3)])
print(ls2[getrandbits(2)])
print(sample(ls2, 1).pop())
