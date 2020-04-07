# TextProBarV2.py
# 文本进度条 单行动态刷新

import time as t
for i in range(101):
    print("\r{:3}%".format(i), end="")
    t.sleep(0.1)