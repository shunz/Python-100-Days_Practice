"""【微实7.3】向文件写入一个列表"""

fname = input('请输入要写入的文件名：')
fo = open(fname, 'w+')
ls = ['唐诗\n', '宋词\n', '元曲\n']
fo.writelines(ls)

fo.seek(0)  # 将文件操作指针返回到文件开始，否则指针一直停留在写入内容的后面，下面代码无法打印出内容
for line in fo:
    print(line)
fo.close()
