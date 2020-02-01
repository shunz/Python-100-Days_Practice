'''
练习5：计算指定的年月日是这一年的第几天
'''

def is_leap_year(year):
    '''
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True, 平年返回False
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几日
    '''

    # 根据是否闰年返回各月天数的列表
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]
    ][is_leap_year(year)]

    # 累加当前月之前所有月份的天数，再加上当前月的对应天数
    # 比如：当前5月20日，累加前4个月的总天数，再加上20天
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

print(which_day(1980, 11, 28))

while True:
    date_input = input('请输入一个格式如1980-11-22的日期：').split('-')
    # 格式转换
    date = [int(x) for x in date_input]
    print(which_day(date[0], date[1], date[2]))
