"""Python isinstance()

- 判断一个对象是否是一个已知的类型，类似type()
    - 与type()区别：
        - type()不会认为子类是一种父类类型，不考虑继承关系
        - isinstance()会认为子类是一种父类类型，考虑继承关系
    - 如果要判断两个类似是否相同推荐使用isinstance()

- 语法：isinstance(object, classinfo)
    - classinfo 可以是：int, float, bool, complex, str, list, tuple, set, dict
"""

a = 2
print(isinstance(a, int))
print(isinstance(a, (str, int,list)))  # 如果是元组中的一个返回 True


# type() 与 isinstance()区别：
class A:
    pass
 
class B(A):
    pass
 
isinstance(A(), A)    # returns True
type(A()) == A        # returns True
isinstance(B(), A)    # returns True
type(B()) == A        # returns False
