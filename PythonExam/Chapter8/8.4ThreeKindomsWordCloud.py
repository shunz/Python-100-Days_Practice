"""8.4 词云是设计和统计的结合，也是艺术与计算机科学的碰撞。
Wordcloud是一款基于Python的词云第三方库，支持对词云数量、背景蒙版，字体颜色
等各种细节的设置，试结合jieba的分词功能构建《三国演义》的词云效果
"""

import jieba.posseg as ps
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

txt = open('threekingdoms.txt', 'r', encoding='utf-8').read()
counts = {}

def wordAndFrequency(items):
    total = 0
    word_frequency = []
    for i in range(20):
        word, count = items[i]
        a = [word, count]
        total += a[1]
        word_frequency.append(a)
    for i in range(20):
        word_frequency[i][1] = word_frequency[i][1]  / total
        word_frequency[i][1] = int(word_frequency[i][1] * 100)
        word_frequency[i][0].encode('utf-8')
        word_frequency[i] = tuple(word_frequency[i])
        print(word_frequency[i])
    return word_frequency

def countFigures():
    words = ps.cut(txt)
    for w in words:
        if len(w.word) == 1:
            continue
        if w.flag == 'nr':
            rword = w.word
            if rword == '玄德' or rword == '玄德曰':
                rword = '刘备'
            if rword == '孔明' or rword == '孔明曰':
                rword = '诸葛亮'
            if rword[-1:] == '兵':
                continue
            counts[rword] = counts.get(rword, 0) + 1
        items = list(counts.items())
        items.sort(key = lambda x:x[1], reverse = True)
        for i in range(20):
            word, count = items[i]
            print('{0:<10}{1:>5}'.format(word, count))
        return wordAndFrequency(items)
    
def generateWordCloud(word_frequency):
    sanguo_color = imread('三国演义.jpg')
    wc = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc',\
                   background_color="black", #可以选择 black 或white\
                   mask = sanguo_color,\
                   random_state=42,\
                   margin=5, width=1800, height=800) # 长宽度控制清晰程度
    wc.generate_from_frequencies(word_frequency)
    image_colors = ImageColorGenerator(sanguo_color)
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    plt.figure()
    plt.show()
word_frequency = countFigures()
generateWordCloud(word_frequency)
