# ------------------------------------------------------------
# map() 函数
#
# https://www.runoob.com/python/python-func-map.html
# ------------------------------------------------------------
"""
- map() 会根据提供的函数对指定序列做映射

- 语法：map(function, iterable, …)
    - function：函数
    - iterable：一个或多个序列
    - 返回值：2.x返回列表，3.x返回迭代器
    
- 第一个参数function以参数序列中的每一个元素调用function函数，返回包含每次
  function函数返回值的新列表
"""

# 实例
def square(x):  # 计算平方数
    return x ** 2
ls = [1,2,3,4,5]

print(list(map(square, ls))) # 计算列表各个元素的平方
# [1,4,9,16,25]

print(list(map(lambda x : x**3, ls)))  # 使用lambda匿名函数计算各元素的立方
# [1, 8, 27, 64, 125]

ls2 = [1,3,5,7,9,11]
print(list(map(lambda x,y : x+y, ls, ls2)))  # 提供两个列表，对相同位置的列表数据进行相加
# [2, 5, 8, 11, 14]

name_list = ['toNy','cHarLiE', 'rAcHaEL']
print(list(map(lambda n : n[0].upper() + n[1:].lower(), name_list)))  # 利用map函数的映射功能规范名字格式
# ['Tony', 'Charlie', 'Rachael']
