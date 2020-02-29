# 集合处理方法
# S.add(x)
# S.discard(x) 若x不存在，不报错
# S.remove(x) 若x不存在，报KeyError异常
# S.clear() 
# S.pop() 随机提取一个元素，若空，报KeyError异常
# S.copy()
# len(S)
# x in S
# x not in S
# set(x) 将其他变量x转为集合类型

A = {'p','y',123}
for item in A:
    print(item, end=',')

print(A)

try:
    while True:
        print(A.pop(),end=',')
except:
    pass

print(A)