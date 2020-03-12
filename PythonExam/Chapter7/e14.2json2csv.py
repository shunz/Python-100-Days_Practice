"""二维json格式转csv格式

- 输入
    - 打开json文件
- 处理
    - 读取文件内容到json库变量中
    - 从变量中分离表头数据和内容数据，放入新列表备用
- 输出
    - 按csv格式，从新列表写入输出文件
"""

import json
fr = open('price.json', 'r')  # 打开json文件
ls = json.load(fr)  # 用json库读取文件内容到列表变量
data = [list(ls[0].keys())]  # 从列表中解析表头内容到新列表
for item in ls:  
    data.append(list(item.values()))  # 遍历列表获得表格内容，追加到新列表中
fr.close()

fw = open('price_from_json.csv', 'w')
for item in data:
    fw.write(','.join(item) + '\n')  # 通过循环将新列表中的内容逐行写入csv文件
    
fw.close()
