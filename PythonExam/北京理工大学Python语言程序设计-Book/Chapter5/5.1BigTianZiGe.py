"""绘制大田字格"""

def draw(n):
    line = 3 * n + 1  # 一共要绘制的行数
    for i in range(1, line+1):
        if i % 3 == 1:  # 判断需要绘制哪种线
            print(n * '+----', end='')
            print('+')
        else:
            print(n * '|    ', end='')
            print('|')

draw(5)
