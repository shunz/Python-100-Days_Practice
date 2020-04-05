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
