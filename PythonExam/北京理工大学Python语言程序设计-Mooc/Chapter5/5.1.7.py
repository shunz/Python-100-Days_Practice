# lambda 函数
# <函数名> = lambda <参数>:<表达式>
# 主要用作一些特定函数或方法的参数，有一些固定使用方式，一般情况，建议使用 def 定义的普通函数 

f = lambda x, y : x + y
print(f(24,34))

f2 = lambda : 'lambda函数'
print(f2())