# --------------------------------------------------
# PEP 289 -- Generator Expressions
#
# https://www.python.org/dev/peps/pep-0289/
# --------------------------------------------------
"""
to be continued...
"""



# --------------------------------------------------
# Generator Expression
#
# https://docs.python.org/3/tutorial/classes.html#generator-expressions
# --------------------------------------------------
"""
Some simple generators can be coded succinctly as expressions using a syntax
similar to list comprehensions but with parentheses instead of square brackets.
These expressions are designed for situations where the generator is used
right away by an enclosing function. Generator expressions are more compact
but less versatile than full generator definitions and tend to be more memory
friendly than equivalent list comprehensions.

Examples:

>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

"""

print(sum(i**2 for i in range(11)))  # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))  # dot product

data = '无锡锡山山无锡，平湖湖水水平湖，常德德山山有德，长沙沙水水无沙，成都毒尘尘有毒'
print(list(data[i] for i in range(len(data)-1, -1, -1)))




# --------------------------------------------------
# 详解Python中的生成器表达式 (generator expression)
#
# https://www.cnblogs.com/shaosks/p/7084748.html
# --------------------------------------------------
"""
- 生成器表达式 (generator expression) 也叫生成器推导式或生成器解析式，用法与列表推导式非常相似。
- 在形式上，生成器推导式使用圆括号(parentheses)作为「定界符 delimiter」，而不是列表推导式所使用的方
  括号(square brackets)
- 与列表推导式最大的不同是，GenExpr的结果是一个生成器对象(generator object)。生成器对象类似于迭代器
  对象，具有惰性求值的特点，只在需要时生成新元素，比列表推导式具有更高的效率，空间占用非常少，尤其适合大数
  据处理的场合。
- 使用生成器对象的元素时，可以根据需要将其转化为列表或元组，也可以使用生成器对象的next()方法或内置函数
  next()进行遍历，或者直接使用for循环遍历其中的元素，但不管哪种方法访问其元素，只能从前往后正向访问每个
  元素，不能再次访问。
- 已访问过的元素，也不支持使用下标访问其中的元素。当所有元素访问结束以后，如果需要重新访问其中的元素，必须
  重新创建该生成器对象，enumerate、filter、map、zip等其他迭代器对象也具有同样的特点
"""

# 1.创建生成器对象
g = ((i+2)**2 for i in range(10))
print(g)
#<generator object <genexpr> at 0x106735450>

# 2.将生成器对象转换为元组
a = tuple(g)
print(a)
#(4, 9, 16, 25, 36, 49, 64, 81, 100, 121)

# 3.生成器对象已遍历结束，没有元素了
print(list(g))
#[]

# 4.重新创建生成器对象
g = ((i+2)**2 for i in range(10))

# 5.使用生成器对象的next()方法获取元素
# 通过 dir(g)发现，3.x中已改为__next__()方法了
print(g.__next__())
#4

# 6.使用内置函数next()获取生成器对象中的元素
print(next(g))
#9

# 7.使用循环直接遍历生成器对象中的元素
for item in g:
    print(item, end=' ')
#16 25 36 49 64 81 100 121

# 8.filter对象也具有类似的特点
x = filter(None, range(20))
print(list(x))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# 9.map对象也具有类似的特点
x = map(str, range(20))
print(list(x))
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', \
#'13', '14', '15', '16', '17', '18', '19']
