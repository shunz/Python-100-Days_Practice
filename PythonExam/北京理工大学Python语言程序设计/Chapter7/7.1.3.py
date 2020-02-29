# 文件的逐行操作

fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
for line in fo:
    print(line)
fo.close()