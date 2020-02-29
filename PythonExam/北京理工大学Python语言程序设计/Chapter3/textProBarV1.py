# TextProBarV1.py
# 文本进度条 简单的开始

import time as t
scale = 10
print("{:-^14}".format('执行开始'))
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    t.sleep(0.1)
print("{:-^14}".format('执行结束'))
