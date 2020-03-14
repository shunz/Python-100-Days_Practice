'''你真的会写项目代码注释么？

https://mp.weixin.qq.com/s/bFUFA8hhySwLwsmvZaf0eg

- 在写实际目代码时，函数(或方法基本都会用到
我们在写项目代码时，函数（或者方法）基本都会用到，一般针对函数我们都需要有文档字符串（可以理解为多行注释），当然如果函数对外部是不可见的，或者短小且容易理解，可以不加文档字符串。

函数的文档字符串应该包含函数的功能（函数做什么）、函数的输入和输出，目标是当别人调用该函数时，不需要看函数代码只看文档字符串即可使用。

当然，对于复杂的函数，除了文档字符串，在函数中的特定区域加入注释也十分重要，可以帮助理解局部的代码内容。

函数的注释常应该包含参数的信息，返回值的信息，异常相关信息，例如：

def check_info(stu_num,stu_info):
    """该函数的作用是通过学生信息字典，通过输入学生学号获取学生的姓名。

    Arguments:
        stu_num {str} -- 学生的学号
        stu_info {dict} -- 学生信息字典

    Returns:
        None or str -- 学生姓名
    """
    if stu_info == None:
        return None
    else:
        stu_name = stu_info.get(stu_num)
        if stu_name == None:
            return ''
        else:
            return stu_name

Args描述了输入参数的类型和含义，Returns描述了输出值的类型和含义，有时还会使用Raises描述了异常信息。

我们常常会使用面向对象编程的方式来写项目代码，那么我们会用到类，类方法等等。

例如：

class Student(object):
    def __init__(self):
        self.stu_info = {}

    def check_info(self, stu_num):
        if self.stu_info == {}:
            return ''
        else:
            stu_name = self.stu_info.get(stu_num)
            if stu_name == None:
                return ''
            else:
                return stu_name

但是接手你项目代码的人去了解你项目这段代码含义是略有困难的，所以不仅为了方便自己阅读代码，并且为了方便他人阅读代码，我们需要使用较为规范的注释方法。

例如我们将该段代码注释后的效果为：

class Student(object):
    """该学生类包含了学生的各种信息
    """

    def __init__(self):
        """该初始化方法用于初始化学生信息
        """
        self.stu_info = {}

    def check_info(self, stu_num):
        """该方法的作用是通过学生信息字典，通过输入学生学号获取学生的姓名。

        Arguments:
            stu_num {str} -- 学生的学号

        Returns:
            str -- 学生姓名
        """
        if self.stu_info == {}:
            return ''
        else:
            stu_name = self.stu_info.get(stu_num)
            if stu_name == None:
                return ''
            else:
                return stu_name

在类的下面应该有一段文档字符串用于描述该类的含义和作用，并且如果类包含公共属性，我们需要在该段文档字符串中加入属性段的注释。
'''



"""PEP 3107 -- Function Annotations

https://www.python.org/dev/peps/pep-3107/
"""
