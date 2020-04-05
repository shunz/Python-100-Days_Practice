"""思考与练习 10.6
这是一个简单的HTML页面，请保存为字符串，完成后面的计算要求

<html>
    <head>
        <title>
            Simple test
        </title>
    </head>
    <body>
        <p id="China">
            中国，<b>你好！</b>。
        </p>
        <p id="World">
            世界，<b>大同！</b>。
        </p>
    </body>
</html>

1. 打印head标签的内容
2. 获取body标签的内容
3. 获取id为China的标签对象
4. 获取并打印HTML页面中的中文字符
"""

import requests
from bs4 import BeautifulSoup
import re

html = '''
<html>
    <head>
        <title>Simple test</title>
    </head>
    <body>
        <p id="China">中国，<b>你好！</b>。</p>
        <p id="World">世界，<b>大同！</b>。</p>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup.head)
print(soup.body)
print(soup.find_all(id='China'))
print(soup.find('p', {'id': 'China'}))
print(soup.find_all(string=re.compile('[\u4e00-\u9fa5]')))
