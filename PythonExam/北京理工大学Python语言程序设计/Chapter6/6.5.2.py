# jieba分词的三种模式：
'''
精确模式（最常用）：把文本精确的切分开，不存在冗余单词
全模式：把文本中所有可能的词语都扫描出来（切分成不同模式，或按不同角度切分变成不同词语），有冗余
搜索引擎模式：在精确模式基础上，对长词再次切分，适合搜索引擎对短词语的索引和搜索，用于特定场合
'''

import jieba

# jieba库常用函数

# jieba.lcut(s) 精确模式，返回一个列表类型的分词结果
print(jieba.lcut('中国是一个伟大的国家'))

# jieba.lcut(s,cut_all=True) 全模式，返回一个列表类型的分词结果，存在冗余
print(jieba.lcut('中华人民共和国是一个伟大的国家', cut_all=True))

# jieba.lcut_for_search(s) 搜索引擎模式，返回一个列表类型的分词结果，存在冗余
print(jieba.lcut_for_search('中华人民共和国是一个伟大的国家'))

# jieba.add_word(w) 向分词词典增加新词w
jieba.add_word('蟒蛇语言')