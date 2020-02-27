"""reduce()函数

https://www.runoob.com/python/python-func-reduce.html
- 对参数序列中元素进行累积
- 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中
的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再
与第三个数据用 function 函数运算，最后得到一个结果。
- 语法：reduce(function, iterable[, initializer])
    - function -- 函数，有两个参数
    - iterable -- 可迭代对象
    - itializer -- 可选，初始参数
"""

"""
Help on built-in function reduce in module _functools:

reduce(...)
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
"""

# 实例
from functools import reduce
def add(x, y) :            # 两数相加
    return x + y

print(reduce(add, [1,2,3,4,5]))   # 计算列表和：1+2+3+4+5

print(reduce(lambda x, y: x+y, [1,2,3,4,5]))  # 使用 lambda 匿名函数
