"""1.8 整数序列求和

用户输入一个正整数N，计算从1到N(包含1和N)相加之后的结果

Input: 用户输入一个正整数N
Process: 从1到N(包含1和N)相加。sum = 1+2+3+…+N
Output: 相加的结果
"""

n = int(input('请输入整数N: '))
sum = 0
# for i in range(n):
#    sum += i + 1
for i in range(n + 1):
    sum += i
print(f'1到N求和结果：{sum}')

