"""Hamlet英文词频统计

    - 输入
        - 从网上找到哈姆雷特全文，保存为hamlet.txt
    - 处理
        1. 分解并提取英文文章的单词
            - 将全文转为小写，排除大小写对词频统计的干扰
                - txt.lower()
            - 将各种特殊字符和标点符号替换为空格，统一分隔方式，便于提取单词
                - txt.replace()
        2. 对每个单词进行计数
            - 将单词保存在变量word中
            - 使用一个字典类型counts={}
            - counts[word] = counts.get(word, 0) + 1  # 新词加入字典，计为1；旧词累加出现次数
        3. 对单词的统计值从高到低进行排序
            - 由于字典类型没有顺序，需要转换为列表类型，然后使用sort()和lambda函数配合实现根据单词出现的次数对元素进行排序
    - 输出
        - 输出前20个高频词语，并格式化打印输出
"""

def getTxt():
    txt = open('hamlet.txt', 'r').read().lower()
    for ch in '!#$%&()*+=,./:;<=>?@[\\]^_`{}|~':
        txt = txt.replace(ch, ' ')  # 将文本中特殊字符替换为空格
    return txt

hamletTxt = getTxt()
words = hamletTxt.split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(f'{word:<10}{count:>5}')
