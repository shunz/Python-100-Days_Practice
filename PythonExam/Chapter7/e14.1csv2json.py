"""csv格式转json格式

- 输入
    - 读入csv文档
- 处理
    - 解析csv格式，将数据内容放入列表
    - 清洗内容，去掉不必要的格式数据
    - 将内容调整成json数据的格式
- 输出
    - 存入json文档

"""

import json
fr = open('price.csv', 'r')
ls = []
for line in fr:
    line = line.replace('\n','')  # 去掉换行符
    ls.append(line.split(','))  # 把数据项逐个分解，放入列表
fr.close()

fw = open('price.json', 'w')
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))  # - zip()是一个内置函数，能够将两个长度相同的列表组合成一个关系对，该函数非常适合于生成键值对
json.dump(ls[1:], fw, sort_keys=False, indent=4, ensure_ascii=False)
fw.close()
