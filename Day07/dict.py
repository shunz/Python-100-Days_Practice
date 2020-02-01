'''
使用字典
'''

# 创建字典的字面量语法
scores = {'Shunz': 95, 'Alex': 80, 'Meya': 88}
print(scores)

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)

# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)

# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)

# 通过键可以获取字典中对应的值
print(scores['Shunz'])

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')

# 更新字典中的元素
scores['Alex'] = 90
scores.update(Candy = 67, Lily = 85)
print(scores)

if 'Meya' in scores:
    print(scores['Meya'])
print(scores.get('Meya'))

# get方法也是通过键获得对应的值，但是可以设置默认值
print(scores.get('Alex1', 60))

# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('Candy', 100))

# 清空字典
scores.clear()
print(scores)

# python123 练习题
d = {'数学': 101, '语文': 202, '英语': 203, '物理': 204, '生物': 206}
# d.update(化学 = 205)
d['化学'] = 205
# d['数学'] = 201
d.update(数学 = 201)
# d.pop('生物')
del d['生物']
for key in d:
    print(f'{d[key]}:{key}')
