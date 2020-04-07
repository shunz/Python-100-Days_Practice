"""e3.1DayDayUp365"""

dayup = (1 + 0.001) ** 365  # 每天提高1‰
daydown = (1 - 0.001) ** 365  # 每天放任1‰
print(f'每天提高1‰，天天向上：{dayup:.2f}, 向下:{daydown:.2f}')


dayup2 = (1 + 0.005) ** 365  # 每天提高5‰
daydown2 = (1 - 0.005) ** 365  # 每天放任5‰
print(f'每天提高5‰，天天向上：{dayup2:.2f}, 向下:{daydown2:.2f}')


dayfactor = 0.01
dayup3 = (1 + dayfactor) ** 365  # 每天提高dayfactor
daydown3 = (1 - dayfactor) ** 365  # 每天放任dayfactor
print(f'每天提高{dayfactor * 100}%，天天向上：{dayup3:.2f}, 向下:{daydown3:.2f}')


dayup4, dayfactor4 = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup4 = dayup4 * (1 - dayfactor4)
    else:
        dayup4 = dayup4 * (1 + dayfactor4)
print(f'向上5天放任2天的力量：{dayup4:.2f}')


def dayUP(df):
    dayup5 = 0.01
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup5 *= 1 - 0.01
        else:
            dayup5 *= 1 + df
    return dayup5

dayfactor5 = 0.01
while dayUP(dayfactor5) < 1.01 ** 365:
    dayfactor5 += 0.001

print(f'努力5天放任2天时，每天的努力参数是：{dayfactor5 * 100:.1f}%,才能与每天努力1%取得的效果一样')
