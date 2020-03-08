"""《三国演义》人物出场统计

    - 输入
        - 从网上找到三国演义全文，保存为threekingdoms.txt
    - 处理
        1. 分解并提取中文文章的单词
            - 采用jieba对文章分词
            - 排除不是人物的单词，用集合类型构建一个排除词汇库
            - 合并同人不同名的单词，比如：刘备=刘玄德=玄德=刘皇叔=主公
        2. 对每个单词进行计数
            - 将单词保存在变量word中
            - 使用一个字典类型counts={}
            - counts[word] = counts.get(word, 0) + 1  # 新词加入字典，计为1；旧词累加出现次数
        3. 对单词的统计值从高到低进行排序
            - 由于字典类型没有顺序，需要转换为列表类型，然后使用sort()和lambda函数配合实现根据单词出现的次数对元素进行排序
    - 输出
        - 输出前10个高频词语，并格式化打印输出
"""

import jieba

excludes = {'却说','将军','二人','不可','荆州','不能','商议','如此','如何','军士','左右','军马','引兵','次日',\
            '大喜','天下','东吴','于是'}

txt = open('threekingdoms.txt', 'r').read().lower()

words = jieba.lcut(txt)
counts = {}

for w in words:
    if w not in excludes and len(w) != 1:
        if w in ['诸葛亮', '孔明曰']:
            w = '孔明'
        elif w in ['关公', '云长']:
            w = '关羽'
        elif w in ['玄德', '玄德曰']:
            w = '刘备'
        elif w in ['孟德', '丞相']:
            w = '曹操'
        counts[w] = counts.get(w, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(9):
    word, count = items[i]
    print(f'{word:<10}{count:>5}')
