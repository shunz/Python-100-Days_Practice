"""1.12 健康食谱输出

列出5种不同食材，输出他们可能组成的所有菜式名称

Input: 内部参数
Process: 两两组合每个食材
Output: 输出所有食材组合名称
"""

diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']

for x in range(5):
    for y in range(5):
        if x != y:
            print(f'{diet[x]}{diet[y]}')
