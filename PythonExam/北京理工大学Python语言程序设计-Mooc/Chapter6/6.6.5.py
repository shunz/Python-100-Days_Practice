# 举一反三练习: 分析19大报告

import jieba

# 导入文本
txt = open('19.txt','r',encoding='utf-8').read()

# 设置需排除的分词集合
# excludes = {'',''}
words = jieba.lcut(txt)

counts = {}
for word in words:
    if len(word) == 1:
        continue
    # 合并同义分词
    # elif word == '' or word == '':
    #     rword = ''
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

# 剔除不想要的分词
# for word in excludes:
#     del counts[word]

# 字典转列表
items = list(counts.items())

# 按分词数从大到小倒排
items.sort(key = lambda x:x[1], reverse = True)

# 
for i in range(20):
    word, count = items[i]
    print('{:<10}{:>5}'.format(word,count))
