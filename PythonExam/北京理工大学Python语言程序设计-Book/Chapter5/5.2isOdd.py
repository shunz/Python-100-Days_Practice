"""实现isOdd()函数，参数为整数，如果为奇数，返回True，否则返回False"""

def isOdd(num):
    try:
        #if type(num) == type(0.):
        if isinstance(num, float):
            raise TypeError
        if num % 2 == 0:
            return False
        else:
            return True
    except TypeError:
        print('This is not a valid int.')
            

print(isOdd(4))
print(isOdd(-1))
print(isOdd('s'))
print(isOdd(3.))
