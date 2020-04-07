# 函数的返回值
# 函数可以返回0个或多个结果

def fact(n, m=1):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s//m, n, m

print(fact(10,5))
# 返回的(725760, 10, 5)是一个元组类型

a,b,c = fact(5,10)
print(a,b,c)