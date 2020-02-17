"""2.1 基本的温度转换程序

"""

def temptrans():
    temp = input('请输入带有符号的温度值(比如82F/C)：')
    if temp[-1] in ['f', 'F']:
        c = (eval(temp[0:-1]) - 32) / 1.8
        print(f'转换后的温度是{c:.2f}°C')
    elif temp[-1] in ['c', 'C']:
        f = 1.8 * eval(temp[0:-1]) + 32
        print(f'转换后的温度是{f:.2f}°F')
    else:
        print('输入格式错误')
        temptrans()

temptrans()
