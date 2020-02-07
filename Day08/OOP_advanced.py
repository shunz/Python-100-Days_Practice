'''
面向对象进阶
'''

'''
@property装饰器

虽然不建议将属性设置为私有的，但直接暴露给外界也是有问题的，比如无法检查赋给属性的值是否有效

建议访问属性通过属性的getter(访问器)和setter(修改器)方法进行对应的操作
要做到这点，可考虑使用@property包装器来包装getter和setter方法，使得对属性的访问及安全
又方便

@property 是一种装饰器，用来修饰方法，创建只读属性，它会将方法转换为同名的只读属性，防止
属性被修改
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


'''
静态方法和类方法

写在类中的方法有三种：
- 对象方法/普通方法：发送给对象的消息，默认有个self参数，只能被对象调用
- 静态方法：用@staticmethod装饰，不带self参数，可以没有参数，可以直接使用类名调用(通过给类发消息来调用)
- 类方法：用@classmethod装饰，默认有个cls参数，可被类和对象调用。
'''
class Classname:
    # 对象方法/普通方法
    def obj(self):
        print('对象方法/普通方法')

    @staticmethod
    def static():
        print('静态方法')

    @classmethod
    def cls(cls):
        print('类方法')


Classname.static()
Classname.cls()

c = Classname()
c.obj()
c.static()
c.cls()


'''
例：三角形类，通过传入三条边长来构造三角形，但传入的三条边长未必能构成三角形对象，因此
可先写入一个方法来验证，这个方法属于三角形类，而不属于三角形对象，因为调用时三角形对象
尚未创建出来，可以通过静态方法解决这类问题
'''

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def tri():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法，但要传入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构成三角形。')

if __name__ == '__main__':
    tri()


'''
类方法：用@classmethod装饰，默认有个cls参数，可被类和对象调用。cls参数代表的是当前类相关
的信息的对象(类本身也是个对象，有的地方也称之为类的元数据对象)，通过此参数可获取和类相关的信息
并可创建出类的对象。
'''

from time import time, localtime, sleep

class Clock(object):
    '''数字时钟'''

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        '''走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour +=1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        '''显示时间'''
        return f'{self._hour:02}:{self._minute:02}:{self._second:02}'


def clock_time():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    clock_time()
    
