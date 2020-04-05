"""
采用from-import导入库中的BeautifulSoup类后，使用BeautifulSoup()创建一个
BeautifulSoup对象
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')  # soup就是一个BeautifulSoup对象

print(type(soup))
print(soup.prettify())

# 几个简单的浏览结构化数据的方法
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['id'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='lh'))

for link in soup.find_all('a'):
    print(link.get('href'))

print(soup.get_text())


# BeautifulSoup对象的常用属性
print(soup.head)
print(soup.title)
print(type(soup.title))  # 每个对应HTML Tag的属性是一个Tag类型
# <class 'bs4.element.Tag'>

print(soup.p)

print(soup.a)
print(soup.a.name)
print(soup.a.attrs)
print(soup.a.string)
print(soup.title.name)
print(soup.title.string)
print(soup.p.contents)

# 需要列出标签对应的所有内容或需要找到非第一个标签时，需要用到BS的find()
# 和find_all()方法，它们会遍历整个HTML文档，按照条件返回标签内容
a = soup.find_all('a')  # 查找所有的<a>
print(len(a))
print(soup.find_all('script'))
print(soup.find_all('input', {'name':'bdorz_come'}))

import re  # 使用正则表达式库，可以用这个库实现字符串片段匹配
# 对标签属性检索时，属性和对应的值采用JSON格式
print(soup.find_all('a', {'name':re.compile('tj_')}))

print(soup.find_all(string=re.compile('百度')))
