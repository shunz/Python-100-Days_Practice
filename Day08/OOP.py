'''
面向对象编程基础
'''

'''
正式的解释：
把一组数据结构和处理它们的方法组成对象(object), 把相同行为的对象归纳为类(class),
通过类的封装(encapsulation)隐藏内部细节，通过继承(inheritance)实现类的
特化(specialization)和泛化(generalization)，通过多态(polymorphism)实现
基于对象类型的动态分派。

所谓「编程」就是程序员按计算机的工作方式控制计算机完成各种任务。

当需要开发一个复杂的系统时，代码的复杂性会让开发和维护工作变得举步维艰，所以，20世纪
60年代末期，「软件危机」、「软件工程」等概念开始出现。

70年代诞生的Smalltalk语言中引入了面向对象编程思想，按此理念，程序中的数据和操作数
据的函数是一个逻辑上的整体，称之为「对象」，而解决问题的方式就是创建出需要的对象，并
向对象发出各种各样的消息，多个对象的协同工作最终可以让我们构造出复杂的系统来解决现实
中的问题。

面向对象也不是解决软件开发中所有问题的最后「银弹」，所以如今的高级程序设计语言几乎都
提供了对多种编程范式的支持，Python也不例外。
'''


'''
类和对象

简单说，类是对象的蓝图和模板，而对象是类的实例。类是抽象的概念，而对象是具体的东西。

在面向对象编程的世界中，一切皆为对象

对象都有属性和方法

每个对象都独一无二

对象一定属于某个类(型)

把一堆拥有共同特征的对象的静态特征(属性)和动态特征(行为)都抽取出来，就可以定义出一
个叫「类」的东西
'''


'''
定义类

用 class 关键字定义类，用函数定义方法，将对象的动态特征描述出来
写在类中的函数，称为(对象的)方法，这些方法就是对象可以接收的消息
'''
class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法可以为 Student 对象绑定 name 和 age 两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}。')


    # PEP 8要求标识符的名字用全小写，多个单词用下划线连接
    # 但部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}只能观看《熊出没》。')
        else:
            print(f'{self.name}正在观看岛国爱情大电影。')


'''
创建和使用对象
'''
def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('Shunz', 39)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_movie消息
    stu1.watch_movie()
    
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()


'''
访问可见性问题

- Python中属性和方法的访问权限只有两种：公开的(public)、私有的(private)，C++、Java、C#等语言还有受保护的(protected)权限
- 公开的方法就是对象能够接受的消息
- 如果希望属性是私有的，给属性命名时用两个下划线作为开头
- 但 Python 并没有从语法上严格保证私有属性和方法的私密性，只是通过换名字来妨碍对其的访问
  只要知道换名字的规则，仍然可以访问到。
- 之所以这么设定，可以用一句名言解释"We are all consenting adults here", 因为绝
  大多数程序员认为开放比封闭好，而且程序员要为自己的行为负责。
- 实际开发中并不建议将属性设为私有，会导致子类无法访问，所以大家会遵循一种命名惯例：以单
  下划线开头表示属性是受保护的，本类之外的代码在访问时应保持慎重。这种做法不是语法上的规
  定，外界是可以访问的，它更多是一种暗示和隐喻。
'''
class Test:

    def __init__(self, foo):
        # 定义私有属性
        self.__foo = foo
        # 定义公开属性
        self.foo = foo

    # 定义私有方法
    def __bar(self):
        print(self.__foo)
        print('__bar')

    # 定义公开方法
    def bar(self):
        print(self.foo)

def main():
    test = Test('hello')
    # AtrributeError: 'Test' object has no attribute '__bar'
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    # print(test.__foo)

    # 调用公开属性/方法
    test.bar()
    print(test.foo)

    # 通过名字规则访问私有属性/方法
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()


'''
'foo': a term used for unimportant variables in programming when the
programmer is too lazy to think of an actual name. The origin of such
word is described in detail in RFC 3092.

The terms 'foobar', 'foo', 'bar', and 'baz' are sometimes used as
placeholder names (also referred to as metasyntactic variables) in
computer programming or computer-related documentation. They have been
used to name entities such as variables, functions, and commands whose
purpose is unimportant and serve only to demonstrate a concept. The
words themselves have no meaning in this usage. Foobar is sometimes
used alone; foo, bar, and baz are sometimes used in that order, when
multiple entities are needed.
'''



'''
面向对象的支柱

三大支柱：封装、继承和多态

封装：隐藏一切可隐藏的实现细节，只向外界暴露(提供)简单的编程接口
- 在类中定义的方法其实就是把数据和对数据的操作封装起来了
- 创建对象后，只需给其发送一个消息(调用方法)就可执行方法中的代码，即：只需知道方法名和
  传参(方法的外部视图)，无需知道方法内部的实现细节(方法的内部视图)
'''


# 练习1：定义一个类描述数字时钟
from time import sleep

class Clock(object):
    '''数字时钟'''

    def __init__(self, hour=0, minute=0, second=0):
        '''初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        '''
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        '''走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        '''显示时间'''
        return f'{self._hour:02}:{self._minute:02}:{self._second:02}'

def main():
    clock  = Clock(23, 59, 55)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
        
            











