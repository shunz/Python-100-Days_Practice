# 程序的异常处理
'''
try:
    num = eval(inpu('请输入一个整数：'))
    print(num ** 2)
except:
    print('输入的不是整数')
'''

# else 语句块在不发生异常时执行
# finally 的语句块一定执行
try:
    n = eval(input())
    print(n/3)
    print('语句块1')
except:
    print('语句块2')
else:
    print('语句块3')
finally:
    print('语句块4')