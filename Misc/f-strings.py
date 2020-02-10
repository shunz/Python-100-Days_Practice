'''
f-strings 格式化字符串文字

格式化字符串字面值 （常简称为 f-字符串）能让你在字符串前加上 f 和
F 并将表达式写成 {expression} 来在字符串中包含 Python 表达式的值。
'''

# 可选的格式说明符可以跟在表达式后面，更好的控制值的格式化方式
import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# 在':'后传递一个整数可以让该字段成为最小字符宽度，在是列对齐时很有用
table = {'Sjoerd': 4127, 'Jack':4098, 'Alxe':7678}
for name, phone in table.items():
    print(f'{name:10}==>{phone:10d}')

# 其他修饰符可用于在格式化之前转化值
# 例如：'!s'应用 str(),'!r'应用 repr(),'!a'应用 ascii()
animals = 'eels'
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.

'''
有关格式规范的参考，请参阅参考指南《格式规格迷你语言》
https://docs.python.org/zh-cn/3/library/string.html#formatspec

详解Python拼接字符串的七种方式
https://www.jiqizhixin.com/articles/2018-11-01-3
'''
