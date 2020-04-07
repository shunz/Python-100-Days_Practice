"""5.6 使用datetime库，对自己的生日输出不少于10种日期格式"""

from datetime import datetime as dt

birthday = dt(1990, 5, 1, 20, 23, 53)
print(birthday)
print('%s年%s月%s日' % (birthday.year, birthday.month, birthday.day))
print('{0:%Y}-{0:%m}-{0:%d} {0:%a}'.format(birthday))
print(f'{birthday:%A}, {birthday:%B} {birthday:%-d}, {birthday:%Y}')
print('{0:%b}.{0:%-d} {0:%Y}'.format(birthday))
#print('{0:%-d}{1} {0:%b} {0:%Y}'.format(birthday, \
#        ['st','nd','rd','th'][birthday.day % 10 - 1 if birthday.day % 10 <= 3 else 3]))
print('{0:%-d}{1} {0:%b} {0:%Y}'.format(birthday, \
        ['st','nd','rd','th'][birthday.day - 1 if birthday.day <= 3 else 3]))
