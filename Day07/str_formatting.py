'''
Python 字符串格式化的三种方式
'''

a, b = 5, 10

# 1. %d
print('%d * %d = %d' % (a, b, a * b))

# 2. {}.format()
print('{0} * {1} = {2}'.format(a, b, a * b))

# 3. f'{a}..{b}' (Python 3.6以后支持)
print(f'{a} * {b} = {a * b}')
