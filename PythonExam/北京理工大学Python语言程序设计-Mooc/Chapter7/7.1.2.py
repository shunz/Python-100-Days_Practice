# 文本文件 vs. 二进制文件
tf1 = open('19.txt','rt')
print(tf1.readline())
tf1.close

tf2 = open('19.txt','rb')
print(tf2.readline())
tf2.close