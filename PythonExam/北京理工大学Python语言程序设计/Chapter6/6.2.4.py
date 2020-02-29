# 元组类型
# 使用()或tuple()创建
# 可以不使用小括号

def func():
    return 1,2 #这里的1,2就是一个元组
print(func())

creatures = 'cat','dog','tiger','human'
print(creatures)

box = 0x0011001,'purple',creatures
print(box)

# 元组类型操作
print(creatures[::-1]) # 取反创建新的元组
print(box[-1][2])