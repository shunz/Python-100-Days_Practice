"""微实例7.2 文本文件逐行打印"""

fname = input('请输入要打开的文件：')
fo = open(fname, 'r')
# print(fo)  # <_io.TextIOWrapper name='m7.1.txt' mode='r' encoding='UTF-8'>
#for line in fo.readlines():  # 将文件的全部内容读入到一个列表中，占用内存多，影响程序执行速度
for line in fo:  # 将文件本身做为一个行序列，遍历所有行，逐行读入内容到内存
    print(line)
fo.close()
