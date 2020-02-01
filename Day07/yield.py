'''
python中yield的用法详解——最简单，最清晰的解释
https://blog.csdn.net/mieleizhi0522/article/details/82142856
'''

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(g.send(7))
print(" "*20)


'''
彻底理解Python中的yield
https://www.jianshu.com/p/d0778f4e055
'''

def g():
    print('1')
    x = yield 'hello'
    print('2, x = ', x)
    y = 5 + (yield x)
    print('3, y = ', y)

f = g()
print(next(f))
print("-"*20)
print(f.send(8))

print("-"*20)
print(f.send(2))
