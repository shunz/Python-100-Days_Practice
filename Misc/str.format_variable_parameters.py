"""Python之format, *args, **kwargs

https://blog.csdn.net/Xin_101/article/details/83784322
"""

""" 1. *args, **kwargs
    - *args和**kwargs是python中的可变参数
    - *args表示任意多个无名参数，tuple类型
    - **kwargs表示关键字参数，dict类型
    - 同时使用时，*args放在**kwargs前面
"""
def foo(*args, **kwargs):
    print("args={}".format(args))
    print("kwargs={}".format(kwargs))
    print('-' * 40)
    
# tuple类型数据
foo(1, 2, 3, 4)

# dict类型数据
foo(a=1, b=2, c=3)

#tuple+dict类型数据
foo(1, 2, 3, 4, a=1, b=2, c=3)

"""Result
args=(1, 2, 3, 4)
kwargs={}
----------------------------------------
args=()
kwargs={'a': 1, 'b': 2, 'c': 3}
----------------------------------------
args=(1, 2, 3, 4)
kwargs={'a': 1, 'b': 2, 'c': 3}
----------------------------------------
"""


""" 2. format
    - format是Python2.6新增的格式化字符串函数，形式str.format()
    - 使用形式'{}{}.format('a','b')
    - 传统%引用变量输出(源于C语言)，即print('%d' % a)
    - format参数个数没有限制
"""
# 默认输出
a = '{},{}'.format('OK','See you later!')
print(type(a))
print(a)

# 指定参数顺序输出
b = '{1} {0}'.format('OK','See you later!')
print(b)

# 指定输出变量
USERINFO = {'name':'Shunz', 'sex':'male'}
print('姓名：{name}, 性别：{sex}'.format(**USERINFO))

# 传入对象参数
class Test(object):
    def __init__(self, value):
        self.value = value
useTest = Test('Here is the value.')
print('{0.value}'.format(useTest))
