# 计算 n! 阶乘

def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

print(fact(4))