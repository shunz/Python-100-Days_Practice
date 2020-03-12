"""Python字符串常用内建函数

https://www.runoob.com/python3/python3-string.html
"""

s = 'steve\t史蒂夫'
s1 = 'steve'
s2 = '史蒂夫'
s3 = '123456'

# capitalize()
print(s.capitalize())

# center(width, fillchar=' ')
print(s.center(20, '$'))

# count(str, beg=0, end=len(string))
print(s.count('e'))

# encode(encoding='utf-8', errors='strict')
# bytes.decode(encoding='utf-8', errors='strict')
"""Python3中没有decode方法，但可以使用bytes对象的decode()方法来解码给定的bytes对
象，这个bytes对象可以由str.encode()方法来编码返回
"""
print(s.encode('utf-8'))
print(s.encode('utf-8').decode('utf-8', 'strict'))

# endswith(suffix, beg=0, end=len(string))
# startswith(subfix, beg=0, end=len(string))
print(s.endswith('史蒂夫'))  # True
print(s.startswith('steve'))

# expandtabs(tabsize=8)
# 把string中的tab符号转为空格，tab符号默认空格数是8
print(s.expandtabs(10))

# find(str, beg=0, end=len(string))
# rfind(str, beg=0, end=len(string))
print(s.find('e'))
print(s.rfind('e'))

# index(str, beg=0, end=len(string))
# rindex(str, beg=0, end=len(string))
print(s.index('e'))
print(s.rindex('e'))

# isalnum()
# 如果字符串至少有一个字符，并且所有字符都是字母alpha或数字num则返回True
print(s.isalnum())
print(s1.isalnum())

# isalpha()
# 如果字符串至少有一个字符，并且所有字符都是字母alpha、汉字或两者组合则返回True
print(s.isalpha())  # False
print('steve'.isalpha())  # True
print('史蒂夫'.isalpha())  # True
print('steve史蒂夫'.isalpha())  # True
print('steve'.encode('utf-8').isalpha())  # True
print('史蒂夫'.encode('utf-8').isalpha())  # False

# isdigit()
print('123456'.isdigit())  # True
print('123456a'.isdigit())  # False

# islower()

# isnumeric()
print('123456'.isnumeric())  # True
print('12345a'.isnumeric())  # False

# isspace()
print(' '.isspace())  # True
print('1 '.isspace())  # False

# title() 返回「标题化」的字符串，即所有单词都是以大写开始，其余字符均为小写
print('this is a title'.title())  # This Is A Title

# istitle()
print('This Is A Title'.istitle())  # True
print('This Is a Title'.istitle())  # False

# isupper()
print('ALL LETTERS ARE UPPER'.isupper())  # True

# join(seq)
print(''.join(str(i) for i in range(10)))

# len(string)

# ljust(width[, fillchar])
# rjust(width[, fillchar])
print('abc'.ljust(10, '*'))
print('abc'.rjust(10, '*'))

# lower()
# swapcase()
# upper()
print('Steve'.lower())  # 'steve'
print('Steve'.swapcase())  # 'sTEVE'
print('Steve'.upper())  # 'STEVE'

# lstrip()
print('  # abc'.lstrip())
print('*# **abc'.lstrip('*'))
# rstrip()
print('  # abc  '.rstrip())
print('*# **abc * #*'.rstrip('*'))
# strip()
print('  # abc  '.strip())
print('*# **abc * #*'.strip('*'))

# maketrans(intab, outtab)
"""创建字符映射的转换表，对于接受两个参数的最简单的调用方式
第一个参数是字符串，表示要转换的字符
第二个参数也是字符串，表示转换的目标
"""
str1 = 'this is string example...wow'
trantab = str1.maketrans('aeiou', '12345')
print(trantab)  # {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
print(str1.translate(trantab))  # th3s 3s str3ng 2x1mpl2...w4w

# translate(table, deletechars='')
# 根据str给出的表(包含256个字符)转换string的字符，要过滤掉的字符放到deletechars参数中
bytes_tabs = bytes.maketrans(b'abcdefg', b'ABCDEFG')  # 制作翻译表
print(b'beekeeper'.translate(bytes_tabs, b'kpr'))

# max(str)
# min(str)

# replace(old, new[,max])
print('beekeeper'.replace('e', 'o', 3))

# split(str='', num=string.count(str))
print('a.b.c.d.e.f.g'.split('.', 3))

# splitlines([keepends=False])
# 按照行('\r','\r\n','\n')分隔，返回一个包含各行作为元素的列表，如果keepends为False，不包含换行符，如果为True，则保留换行符
print('abc\n\ndefg\rhijkl\r\nmn'.splitlines())
print('abc\n\ndefg\rhijkl\r\nmn'.splitlines(True))

# zfill(width)
# 返回长度为width的字符串，原字符串右对齐，前面填充0
print('abc'.zfill(10))  # '0000000abc'

# isdecimal()
# 检查字符串是否只包含十进制字符
print('123'.isdecimal())  # True
print('1240s'.isdecimal())  # False
