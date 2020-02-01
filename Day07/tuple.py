'''
使用元组
'''

# 定义元组
t = ('Shunz', 39, True, '四川成都')
print(t)

# 获取元组中的元素
print(t[0])
print(t[3])

# 遍历元组中的值
for member in t:
    print(member)

# 重新给元组赋值
# t[0] = '王大锤'  # TypeError

# 变量t重新引用了新的元组，原来的元组将被垃圾回收
t = ('王大锤', 20, True, '湖北武汉')
print(t)

# 将元组转换成列表
person = list(t)
print(person)

# 将列表转换成元组
person[0] = '李港生'
person[1] = 25
person[3] = '中国香港'
person_tuple = tuple(person)
print(person_tuple)

import sys
print(sys.getsizeof(person))
print(sys.getsizeof(person_tuple))

'''
可在ipython中使用魔法指令%timeit来分析创建同样内容的元组和列表所花费的时间
%timeit [1,2,3]
%timeit (1,2,3)
'''

