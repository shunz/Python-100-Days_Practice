str = '一二三456七八九'

print(len(str))

# 整数100的十六进制或八进制小写形式字符串
print(hex(100))
print(oct(100))

# chr函数返回 Unicode 编码对应的字符
print(chr(0))
print(chr(33))
print(chr(34))
print(chr(1099))
print(chr(9800))
print(chr(18888))
print(chr(10004))
print(chr(1114111))

# ord函数返回字符对应的 Unicode 编码
print(ord('中'))
print(ord('0'))
print(ord('a'))
print(ord('A'))
print(ord('•'))
print(ord('√'))

# 一些有趣的例子
print('1+1=2 '+chr(10004))

# 遍历显示表示星座的12个字符
for i in range(12):
    print(chr(9800+i), end='-')

# 转换字符大小写
char = 'AbCdEfGhIjKlMn'
print(char.lower())
print(char.upper())

# 返回一个列表，由被某分隔符分隔的部分组成
print('A,b,C,d,E,f'.split(','))

# 返回子串出现的次数
print('An apple a day'.count('a'))

# 返回字符串副本，所有old子串替换为new
print('Python'.replace('n','n123.io'))

# 字符串根据width居中，填充字符可选
print('Python'.center(20,'•'))

# 从str头尾中去掉列出的字符，中间字符不能删除
print('-4=  p4yath-on-=a   '.strip(' =a4-'))

# 除最后元素外每个元素后增加一个str
print(','.join('123456'))