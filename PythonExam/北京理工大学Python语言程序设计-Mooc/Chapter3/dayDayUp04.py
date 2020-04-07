# DayDayUp04.py

def dayUP(df):
    dayup = 1
    for i in range(365):
        # 三天打鱼，两天晒网
        if i % 5 in [3,4]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    print(dayup)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < pow(1.01,365):
    dayfactor += 0.0001
print("工作日的努力参数是：{:.3f},以此坚持365天能产生{:.2f}倍力量。".format(dayfactor, (1 + dayfactor) ** 365))