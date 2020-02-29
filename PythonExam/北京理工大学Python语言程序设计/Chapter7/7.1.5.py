# 数据的文件写入

fo = open('output.txt', 'w+')
ls = ['中国','法国','美国']
fo.writelines(ls)
fo.seek(0) # 指针移至文件初始位置
for line in fo:
    print(line)
fo.close()
