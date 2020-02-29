# 三位水仙花数
# "水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。
# 请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪
s = ''
for i in range(100,1000):
    strI = str(i)
    if eval(strI[0]) ** 3 + eval(strI[1]) ** 3 + eval(strI[2]) ** 3 == i:
        s += '{},'.format(i)
# 采用s[:-1]方式不输出最后一个逗号
print(s[:-1])


# 把所有结果放到一个列表中，采用字符串的.join()方法输出结果。
ls = []
for i in range(100,1000):
    strI = str(i)
    if eval(strI[0]) ** 3 + eval(strI[1]) ** 3 + eval(strI[2]) ** 3 == i:
        ls.append(str(i))
print(','.join(ls))