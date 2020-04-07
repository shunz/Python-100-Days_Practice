"""将CSV文件转换成HTML文件

- 输入
    - 读入csv文件
- 处理
    - 读取文件数据到列表
    - 对数据进行格式处理和转换
- 输出
    - 输出HTML格式文件
"""

header = '''<!DOCTYPE HTML>
<html>
  <body>
    <meta charset=utf-8>
    <h2 align=center>20xx年x月部分大中城市新建住宅价格指数</h2>\n'''  # html文件头部标记内容

footer = '''    </table>
  </body>
</html>\n'''  # html文件尾部标记内容

def fill_data(data):  # 生成一行表格内容+表格格式
    return '''      <tr>
        <td align="center">{}</td>
        <td align="center">{}</td>
        <td align="center">{}</td>
        <td align="center">{}</td>
      </tr>\n'''.format(*data)

fr = open('price.csv', 'r')
ls = []
for line in fr:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fr.close()

fw = open('price.html', 'w')  # w: 只要没有close，可以一直写新内容
fw.write(header)
fw.write('''    <table border='1' align="center" width=70%>\n\
      <tr bgcolor='orange'>
        <th width="25%">{}</th>
        <th width="25%">{}</th>
        <th width="25%">{}</th>
        <th width="25%">{}</th>
      </tr>\n'''.format(*ls[0]))  # 生成表格格式 + <th>表格表头的一列

for i in range(len(ls)-1):  # 循环生成<td>表格内容的n列
    fw.write(fill_data(ls[i+1]))
fw.write(footer)

fw.close()
