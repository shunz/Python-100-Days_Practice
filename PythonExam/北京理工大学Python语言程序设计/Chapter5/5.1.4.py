# 计算 n!//m

# 定义可选参数，放在必选参数后面
def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m
     
print(fact(10))
print(fact(10,10))

# 参数传递的两种方式，函数调用时，
# 参数可以按照位置或名称传递
print(fact(m=20,n=10))


# 可变参数传递
# 计算 n!乘数
def fact2(n, *b):
    s = 1
    for i in range(1, n+1):
        s *= i
    for item in b:
        s *= item
    return s

print(fact2(10))
print(fact2(10,3))
print(fact2(10,3,5,8))