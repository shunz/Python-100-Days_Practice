"""用递归计算阶乘"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = eval(input('请输入一个整数：'))
    print(f'{abs(int(num))}的阶乘是{factorial(abs(int(num)))}')

while 1:
    main()
