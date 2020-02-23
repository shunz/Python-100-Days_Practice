# ------------------------------------------------------------
# filter() 函数
#
# https://www.runoob.com/python3/python3-func-filter.html
# ------------------------------------------------------------
"""
- filter()用于过滤序列，过滤掉不符合条件的元素，返回由条件元素组成的新列表(2.x)/一个迭代器对象(3.x),可
  用list()转换为列表

- 语法：filter(function, iterable)
    - function: 判断函数
    - iterable: 可迭代对象
    - 返回值：2.x返回列表，3.x返回迭代器

- 第一个参数为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True或False，然后
  将返回True的元素放到新列表中
"""

# 实例1：过滤出列表中的所有奇数
def is_odd(n):
    return n % 2 == 1

tmplist = filter(is_odd, range(1,11))
newlist = list(tmplist)
print(newlist)
#[1, 3, 5, 7, 9]

# refactor the example above
print(list(filter(lambda n: n % 2 == 1, range(1,11))))


# 实例2：过滤出1~100中平方根是整数的数
print(list(filter(lambda n: n ** 0.5 % 1 == 0, range(1,1001))))
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
