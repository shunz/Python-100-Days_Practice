# 局部和全局变量

# 规则1：局部变量和全局变量是不同的变量（即使同名）
# 可使用global保留字声明全局变量

n,s = 10,100
def fact(n):
    global s
    for i in range(1, n+1):
        s *= i
    return s
print(fact(n),s)  #此处全局变量s被函数修改

# 规则2：局部变量为组合数据类型且未创建，等同于全局变量
ls = ['F','f']
def func(a):
    ls.append(a)
    return
func('C')
print(ls)

ls2 = ['F','f']
def func2(a):
    ls2 = []
    ls2.append(a)
    print(ls2)
    return
func2('C')
print(ls2)
