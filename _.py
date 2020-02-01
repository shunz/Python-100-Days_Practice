'''
封装、解构、丢弃变量

1. 从lst=list(range(10))列表中取出第二个、第四个、以及倒数第二个元素
2. 从lst=[1,(2,3,4),5]中，提取4
3. 从/etc/sysconfig/network-scripts/ifcfg-eth0中获取ifcg-eth0

Ver: 0.1
Author: Shunz
Last_update: 2020-01-10
'''

# 1
lst = list(range(10))
_, a, _, b, *_, c, _ = lst
print(a,b,c)

# 2
lst2 = [1,(2,3,4),5]
_,(*_,d),_= lst2
print(d)


# 3
s = '/etc/sysconfig/network-scripts/ifcfg-eth0'
*_,e = s.split('/')
print(e)
