'''
面向对象进阶
'''

'''
@property装饰器

虽然不建议将属性设置为私有的，但直接暴露给外界也是有问题的，比如无法检查赋给属性的值是否有效

建议访问属性通过属性的getter(访问器)和setter(修改器)方法进行对应的操作
要做到这点，可考虑使用@property包装器来包装getter和setter方法，使得对属性的访问及安全
又方便
'''


'''
__slots__魔法

Python是一门动态语言，动态语言允许在程序运行时给对象绑定新的属性或方法，或对已经绑定的
属性和方法进行解绑定。

可以通过在类中定义__slots__变量来限定自定义类型的对象只能绑定某些属性。
注意：__slots__限定只对当前类的对象生效，对子类不起作用。
'''

class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')
    
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} {self._age} 岁了，正在玩飞行棋。')
        else:
            print(f'{self._name} {self._age} 岁了，正在玩斗地主。')


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳' # AttributeError: can't set attribute
    person._gender = '男'
    print(f'{person._name}的性别是:{person._gender}')
    if person._gender == '男' and person._age >= 18:
          print(f'{person._name}已经是个{person._age}岁的{person._gender}性了，可以……')
    # person._is_gay = True # AttributeError: 'Person' object has no attribute '_is_gay'
    
if __name__ == '__main__':
    main()





