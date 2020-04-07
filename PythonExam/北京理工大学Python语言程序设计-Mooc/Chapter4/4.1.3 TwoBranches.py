# 二分支结构的紧凑形式
# <表达式1> if <条件> else <表达式2>

print('right' if True else 'wrong')

guess = eval(input())
print('猜{}了'.format('对' if guess == 99 else '错'))