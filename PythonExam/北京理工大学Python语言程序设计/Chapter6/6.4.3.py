# 字典类型操作函数和方法
'''
- del d[k] 删除键k对应值
- k in d 判断键k是否在字典d中
- d.keys() 返回d中所有键信息
- d.values() 返回d中所有值信息
- d.items() 返回字典d中所有键值对信息
- d.get(k,<default>) 键k存在，返回对应值，不存在则返回<default>值
- d.pop(k,<default>) 键k存在，取出对应值，并删除该键值对，不存在则返回<default>值
- d.popitem() 随机从d中取出一个键值对，以元组形式返回
- d.clear() 删除所有的键值对
- len(d) 返回d中元素个数
'''

d = {'China':'Beijing', 'US':'Washionton', 'France':'Paris','Japan':'Tokyo', 'Korea':'Seaul'}

print(len(d))
del d['US']
print('US' in d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get('US','US does not exist.'))
print(d.pop('France','France does not exist.'))
print(d)
print(d.popitem())
print(len(d))

d.clear()
print(d)
d['England'] = 'London'
d['Canada'] = 'Toto'
print(d)
d['Canada'] = 'Toranto'
