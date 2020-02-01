'''
enumerate()函数

- Python 内置函数
- 描述：用于将一个可遍历的数据对象(如：列表、元组或字符串)组合成一个索引序列，同时列出数据和数据下标，一般用在for循环中
- 语法：enumerate(sequence, [start = 0])
- 参数：sequence -- 一个序列、迭代器或其他支持迭代对象
       start -- 下标起始位置
- 返回值：返回 enumerate(枚举)对象
'''

# 实例
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
# 下标从 1 开始
print(list(enumerate(seasons, start = 1)))

# for循环使用enumerate
for index, element in enumerate(seasons):
    print(index, element)
    print(index, seasons[index])
