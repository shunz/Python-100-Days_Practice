"""一维数据写入CSV文件"""

fo = open('price_cd.csv', 'w')
ls = ['成都','104.7','79.5','128.2']
fo.write(','.join(ls) + '\n')
fo.close()
