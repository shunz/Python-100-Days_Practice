"""随机密码生成

在26个字母大小写和9个数字组成的列表中随机生成10个8位密码

- 输入
    - 无
- 处理
    - 生成由26个和9个数字组成的列表
    - 从列表中随机取8个字符生成一个密码
- 输出
    - 打印显示10个密码
"""
import random as r

#alphas = 'abcdefghijklmnopqrstuvwxyz'
lowerAlpha = ''.join([chr(ord('A')+i) for i in range(26)])
upperAlpha = ''.join([chr(ord('a')+i) for i in range(26)])
#nums = '0123456789'
num = ''.join([chr(ord('0')+i) for i in range(10)])
ls = lowerAlpha + upperAlpha + num

for _ in range(10):
    psd = ''
    for _ in range(8):
        psd += ls[r.randint(0, len(ls)-1)]
    print(psd)


# 1st refactor
A = ord('A')
a = ord('a')
zero = ord('0')
for i in range(10):
    psd = ''
    for _ in range(8):
        psd += chr(r.choice(list(range(A, A + 25)) + list(range(a, a + 25)) \
                            + list(range(zero, zero + 9))))
    print(f'密码{i+1:02}:{psd}')


# 2nd refactor
A2Z = list(range(ord('A'), ord('A') + 25))
a2z = list(range(ord('a'), ord('a') + 25))
num = list(range(ord('0'), ord('0') + 9))
for i in range(10):
    code = ''.join(chr(r.choice(A2Z + a2z + num)) for _ in range(8))
    print(code)
