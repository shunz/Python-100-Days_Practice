'''
Python 代码规范
https://juejin.im/post/593ebd7eac502e006b520a8f
'''

# ==================================================
# 1. 编码
# 
# • 如无特殊情况，文件一律用 UTF-8 编码
# • 如无特殊情况，文件头必须加入 # -*- coding: utf-8 -*-
# ==================================================

# ==================================================
# 2.1 缩进
# 
# • 统一使用 4 个空格进行缩进
# ==================================================

# ==================================================
# 2.2 行宽
# 
# • 每行代码尽量不超过 80 个字符
#   理由：
#     * 查看 side-by-side 的 diff 时很有帮助
#     * 方便在控制台下查看代码
#     * 太长可能是设计有缺陷
# ==================================================

# ==================================================
# 2.3 引号
# 
# • 自然语言使用双引号 "……"，例如：u"你好世界"
# • 机器标识使用单引号 '……', 例如：dict 里的 key
# • 正则表达式使用原生的双引号 r"……"
# • 文档字符串(docstring)使用三个双引号 """………"""
# ==================================================

# ==================================================
# 2.4 空行
# 
# • 模块级函数和类定义之间空两行
# • 类成员函数之间空一行
# ==================================================
class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass


# ==================================================
# 3.1 import
# 
# • import 语句应该分行书写
# • import 语句应该使用 absolute import
# • import 应在文件头部，模块说明及docstring之后，全局变量之前
# • import 语句应按顺序排列，每组之间用一个空行分隔
# • 如果发生命名冲突，则可以使用命名空间
# ==================================================

# 正确写法
import os
import sys

from time import time
import foo.bar import Bar

import bar
import foo.bar

# 不推荐的写法
import sys,os
import ..bar import Bar


# ==================================================
# 4. 空格
# 
# • 在二元运算符两边各空一格(=,-,+=,==,>,in,is not,and)
# • 函数的参数列表中，','之后要有空格
# • 函数的参数列表中，默认值等号两边不要添加空格
# • 左括号之后，右括号之前不要加多余空格
# • 字典对象的左括号之前不要多余的空格
# • 不用为对齐赋值语句而使用额外空格
# ==================================================

# 正确写法
i = i + 1
def complex(real, imag=0.0):
    pass
spam(ham[1], {eggs: 2})
dict['key'] = list[index]

# 不推荐的写法
i=i+1
def complex(real,image = 0.0):
    pass
spam( ham[1], { eggs : 2 } )
dict ['key'] = list [index]
x        = 1
y        = 2
long_var = 3

# ==================================================
# 5. 换行
# ==================================================
# • Python 支持括号内的换行
# 1) 第二行缩进到括号的起始处
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 2) 第二行缩进4个空格，适用于起始括号就换行的情形
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# 使用反斜杠 \ 换行，二元运算符 + . 等应出现在行末; 长字符串也可用此法换行
session.query(MyTable).\
        filter_by(id=1). \
        one()

print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')

# 禁止符合语句，即一行中包含多个语句
do_first(); do_second(); do_third();

# if/for/while 一定要换行
if foo == 'blah': do_blash_thing()


# ==================================================
# 6. docstring
#
# • 所有的公共模块、函数、类、方法，都应该写 docstring。私有方法
#   不一定需要，但应该在 def 后提供一个块注释来说明。
# • docstring 的结束"""应该独占一行，除非此docstring只有一行
# ==================================================
"""Return a foobar
Optional plotz says to frobnicate the bizbaz first.
"""

"""Oneline docstring"""


# ==================================================
# 7. 注释
# ==================================================

# • 块注释："#"号后空一格，段落间用空行分开(同样需要"#"号)
# 块注释
# 块注释
#
# 块注释
# 块注释

# • 行注释：至少使用两个空格和语句分开，不要使用无意义的注释
x = x + 1  # 边框加粗一个像素

# • 比较重要的注释段，使用多个等号隔开，可以更醒目，突出重要性
# ==================================================
# 请勿在此处添加 ………… 等行为！！！
# ==================================================


# ==================================================
# 8. 文档注释(Docstring)
#
# 一般出现在模块、类、函数的头部，在python中可以通过对象的
# __doc__ 对象获取文档; 编辑器和IDE也可根据Docstring给出自
# 动提示
# ==================================================

# docstring以"""开头和结尾，首行不换行，若有多行，末行必需换行
# 以下是 Google 的 docstring 风格示例

# -*- coding: utf-8 -*-
"""Example docstrings.

This module demonstrates documentation as specified by
the `Google Python Style Guide`. Docstrings may extend
over multiple lines. Sections are created with a section
header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or
    ``Examples`` sections. Sections support any
    reStructuredText formatting, including literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text.
Section breaks are also implicitly created anytime a new
section starts.
"""

# 不要在docstring复制函数定义原型，而是具体描述其具体内容，解释具体
# 参数和返回值等
def function(a, b):
    """计算并返回a到b范围内数据的平均值"""
    ………
        
# 对函数参数、返回值等的说明采用 numpy 标准，如下所示
def func(arg1, arg2):
    """在这里写函数的一句话总结(如：计算平均值)。

    这里是具体描述

    参数
    ----------
    arg1: int
        arg1的具体描述
    arg2: int
        arg2的具体描述

    返回值
    ----------
    int
        返回值的具体描述

    参看
    ----------
    otherfunc: 其他关联函数等…

    示例
    ----------
    示例使用doctest格式，在`>>>`后的代码可以被文档测试工具作为测试
    用例自动运行

    >>> a=[1,2,3]
    >>> print [x ]+ 3 for x in a]
    [4, 5, 6]
    """

# docstring 不限于中英文，但不要中英文混用

# docstring 不是越长越好，通常一两句话能把情况说清楚即可

# 模块、公用类、公用方法，能写 docstring 的，应尽量写


# ==================================================
# 9. 命名规范
# ==================================================

# 9.1 模块名：尽量使用小写命名，首字母保持小写，尽量不用下划线(除非多个单
# 词，且数量不多的情况)

import decoder
import html_parser

# 可将相关的类和顶级函数放在同一个模块里，不像Java，没必要限制一个
# 类一个模块

# 9.2 类名：使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一
# 个下划线开头
class _AnimalFarm(Farm):
    pass

# 9.3 函数名：一律小写，如有多个单词，用下划线隔开
def _run_with_evn():
    pass

# 9.4 变量名：尽量小写，多个单词用下划线隔开

# 9.5 常量名：采用全大写
MAX_CLIENT = 100
MAX_CONNECTION = 1000
CONNECTION_TIMEOUT = 600



