"""逐行处理CSV格式数据

逐行读取CSV文件，逐行运算处理
"""

fo = open('price.csv', 'r')

for line in fo:
    line = line.replace('\n', '')
    ls = line.split(',')
    lns = ''
    for s in ls:
        lns += f'{s}\t'
    print(lns)
fo.close()
