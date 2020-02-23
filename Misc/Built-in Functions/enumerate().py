"""Python enumerate()

https://www.runoob.com/python3/python3-func-enumerate.html

- 用于将一个可遍历的数据对象，如：列表、元组或字符串，组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
- 语法：enumerate(sequence, [start=0])
    - sequence: 一个序列、迭代器或其他支持迭代对象
    - start：下标起始位置
    - 返回值：enumerate(枚举)对象
"""

# 实例
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1)))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


# 用 enumerate 和字典表达式将列表转成字典
fruits = ['orange', 'grape', 'pitaya', 'blueberry']
print(dict(enumerate(fruits)))  # {'orange': 0, 'grape': 1, 'pitaya': 2, 'blueberry': 3}
print({fruit:index for index, fruit in enumerate(fruits)})  # {0: 'orange', 1: 'grape', 2: 'pitaya', 3: 'blueberry'}
