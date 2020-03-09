"""微实例7.1 理解文本文件和二进制文件的区别"""

textFile = open('m7.1.txt', 'rt')  # t表示文本文件方式
print(textFile.readline())  # 中国是个伟大的国家
textFile.close()

binFile = open('m7.1.txt', 'rb')  # b表示二进制文件方式
print(binFile.readline())  # b'\xe4\xb8\xad\xe5\x9b\xbd\xe6\x98\xaf\xe4\xb8\xaa\xe4\xbc\x9f\xe5\xa4\xa7\xe7\x9a\x84\xe5\x9b\xbd\xe5\xae\xb6'
binFile.close()
