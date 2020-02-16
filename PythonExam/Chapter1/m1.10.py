"""1.10 阶乘求和

计算 1+2!+3!+…+10!的结果

Input: 内部参数
Process: 累加阶乘之和
Output: 显示累加结果
"""

sum = 0
tmp = 1
for i in range(1, 11):
    tmp *= i
    sum += tmp
print(f'运算结果是：{sum}')
