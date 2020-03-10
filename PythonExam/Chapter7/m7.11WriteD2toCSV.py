"""二维数据写入CSV文件

读入price.csv文件，将其中的数据读出，将数字部分计算百分比后输出到price_out.csv

- 输入
    - 读入price.csv文件
- 处理
    - 读出数字部分到列表
    - 对列表中元素逐行判断，对浮点数值进行百分比计算
    - 运算结果写回列表，重新组织成二维数据形式
- 输出
    - 输出到price_out.csv文件
"""

fr = open('price.csv', 'r')
fw = open('price_out.csv', 'w')

ls = []
for line in fr:  # 将csv文件中的二维数据读入到列表变量
    line  = line.replace('\n', '')
    ls.append(line.split(','))

for i in range(len(ls)):  # 遍历列表变量计算百分比
    for j in range(len(ls[i])):
        if ls[i][j].replace('.', '').isnumeric():  # isnumeric()无法判断浮点数，这里用了点dirty coding trick,是一种不完备的判断方式，但在该例的应用背景下可用
            ls[i][j] = f'{float(ls[i][j])/100:.1%}'

for row in ls:  # 将列表变量中的两位数据输出到csv文件
    print(row)
    fw.write(','.join(row) + '\n')

fr.close()
fw.close()
