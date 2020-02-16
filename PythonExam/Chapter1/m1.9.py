"""1.9 九九乘法表输出

工整打印输出常用的九九乘法表，格式不限

Input: 内部参数
Process: 逐行打印乘法口诀
Output: 显示打印结果
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}={i * j:<2}', end='  ')
    print(' ')
