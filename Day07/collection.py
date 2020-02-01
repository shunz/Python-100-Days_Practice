'''
使用集合
'''

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length = ', len(set1))

# 创建集合的构造器语法(面向对象范畴)
set2 = set(range(1, 10))
set3 = set((1,2,3,3,2,1))
print(set2, set3)

# 创建集合的推导式语法(推导式也可用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

'''
向集合添加元素和从集合删除元素
'''
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

'''
集合的成员、交集、并集、差集等运算
'''
# 集合的交集
print(set1 & set2)
# 对集合运算时可调用集合对象的方法，和使用对应的运算符作用是一样的，但运算符更直观
print(set1.intersection(set2)) 

# 集合的并集
print(set1 | set2)
print(set1.union(set2))

# 集合的差集
print(set1 - set2)
print(set1.difference(set2))

# 集合的对称差运算
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 判断子集和超集
print(set2 <= set1)
print(set2.issubset(set1))

print(set1 >= set2)
print(set1.issuperset(set2))
