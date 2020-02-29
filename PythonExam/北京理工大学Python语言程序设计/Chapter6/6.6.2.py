# 文本词频统计
'''
英文文本：Hamlet 分析词频
http://python123.io/resources/pye/hamlet.txt

中文文本：三国演义 分析人物
http://python123.io/resources/pye/threekingdoms.txt
'''

def getText():
    txt = open('hamlet.txt', 'r').read()
    # 大写转小写
    txt = txt.lower() 
    # 特殊字符替换为空格
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}~':
        txt = txt.replace(ch,'')
    return txt # 归一化结果
    
hamletText = getText()
words = hamletText.split() # 所有单词的列表

counts = {} # 新建字典放每个单词的词频数
for word in words:
    counts[word] = counts.get(word,0) + 1

# 将字典转换成列表，便于排序
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) # 将列表按键值对的第2个元素进行排序，由大到小倒排 

# print(items[:10])

for i in range(20):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))
