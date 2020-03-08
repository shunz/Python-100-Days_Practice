"""求解一组不定长数据的基本统计值(平均值、标准差、中位数

输入：从用户输入、文件、网络等途径获取一组数据
处理：适当的数据结构和算法
输出：平均值、标准差和中位数
"""

from math import sqrt
def getNum():  # 获取用户输入
    nums = []
    numStr = input('请输入数字(直接输入回车退出)：')
    while numStr != '':
        nums.append(eval(numStr))
        numStr = input('请输入数字(直接输入回车退出)：')
    return nums

def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean)**2
    return sqrt(sdev / (len(numbers) - 1))

def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()  # 主体函数
m = mean(n)
print(f'平均值：{m:.2f}，方差：{dev(n,m):.2f}，中位数：{median(n)}')
