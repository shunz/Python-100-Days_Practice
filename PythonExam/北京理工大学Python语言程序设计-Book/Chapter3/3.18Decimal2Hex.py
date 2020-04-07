# 十进制转十六进制
x16 = '0123456789abcdef'
x = int(input('请输入一个正的十进制数：'))
out = ''
if x is 0:
    print('结果是0x0')
else:
    while x:
        remainder = int(x % 16)
        out = str(x16[remainder]) + out
        x = (x - remainder)/16
    print(f'结果是0x{out}')
    
