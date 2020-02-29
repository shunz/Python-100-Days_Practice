# Random 库包括两类函数
# 基本随机数函数 seed(),random()
# 扩展随机数函数 randint(), getrandbits(), uniform(), randrange(), choice(), shuffle()

import random

# seed()
# 初始化给定的随机数种子，默认为当前系统时间
print(random.seed(10))
print(random.seed())

# random()
# 生成一个[0.0, 1,0)之间的随机小数
print(random.random())
print(random.random())

# randint(a,b) 
# 生成一个[a,b]之间的整数
print(random.randint(10,100))

# randrange(m,n[,k])
# 生成一个[m,n)之间1️以k未步长的随机整数
print(random.randrange(10,100,3))

# getrandbits(k)
# 生成一个k比特长的随机整数
print(random.getrandbits(10))

# uniform(a,b)
# 生成一个[a,b]之间的随机小数
print(random.uniform(10,100))

# choice(seq)
# 从序列seq中随机选择一个元素
print(random.choice([1,2,3,4,5,6,7,8,9]))

# shuffle(seq)
# 将序列seq中元素随机排列，返回打乱后的序列
s = [1,2,3,4,5,6,7,8,9];random.shuffle(s);print(s)