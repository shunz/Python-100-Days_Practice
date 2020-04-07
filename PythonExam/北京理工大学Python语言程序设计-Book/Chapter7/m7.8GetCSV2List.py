"""导入CSV格式数据到列表"""

fo = open('price.csv', 'r')
ls = []
for line in fo:
    line = line.replace('\n', '')
    ls.append(line.split(','))
print(ls)
fo.close()
