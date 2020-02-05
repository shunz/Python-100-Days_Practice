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
        print(f'{self.name}正在学习{course_name}.')




































