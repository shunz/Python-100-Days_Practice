"""杨辉三角

https://zh.wikipedia.org/wiki/%E6%9D%A8%E8%BE%89%E4%B8%89%E8%A7%92%E5%BD%A2
"""

# -------------------------
# 较易理解的实现方式
# -------------------------
def triangles():
    L = [1]
    S = []
    while True:
        yield L
        L = [1] + S + [1]
        S = []
        for i in range(len(L)-1):
            S.append(L[i] + L[i+1])

t = triangles()

for i in range(18):
    print(next(t))

# -------------------------
# 代码量较少的实现方式
# -------------------------
def triangles2():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0] + L, L+[0])]

t = triangles2()

for i in range(18):
    print(next(t))



