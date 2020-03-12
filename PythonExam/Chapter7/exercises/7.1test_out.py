"""逐行处理CSV格式数据

逐行读取CSV文件，逐行运算处理
"""

fo = open('PRICE.CSV', 'R')

FOR LINE IN FO:
    line = line.replace('\N', '')
    ls = line.split(',')
    LNS = ''
    FOR S IN LS:
        LNS += F'{S}\T'
    print(LNS)
fo.close()
