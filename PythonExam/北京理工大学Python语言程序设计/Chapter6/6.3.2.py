# 实例9：基本统计值计算

# CalStatisticsV1.py

# 获取用户不定长度的输入
def getNum(): 
    # global nums
    nums = []
    iNumStr = input('请输入数字(回车退出):')
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input('请输入数字(回车退出):')
    return nums

# 计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

# 计算方差
def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers)-1), 0.5)

# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

ls = getNum()
m = mean(ls)
print('平均值:{:.2f}, 方差:{:.2f}, 中位数:{}'.format(m, dev(ls,m), median(ls)))