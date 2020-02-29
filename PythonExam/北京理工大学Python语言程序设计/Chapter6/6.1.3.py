# 集合操作符
# S|T 并集
# S-T 差集
# S&T 交集
# S^T 补集
# S<=T / S<T 判断子集关系
# S>=T / S>T 判断包含关系

# 增强操作符
# S|=T 更新S，包括S和T中的所有元素
# S-=T 更新S，包括在S但不在T中的元素
# S&=T 更新S，包括同时在S和T中的元素
# S^=T 更新S，包括S和T中的非相同元素

a = {'p','y',123}
b = set('pypy123')
print(a-b)
print(b-a)
print(a&b)
print(a|b)
print(a^b)
a^=b
print(a)