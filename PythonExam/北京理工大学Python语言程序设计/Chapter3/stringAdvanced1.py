str = "1234567890"

# 正向递增序号
print(str[1])

# 反向递减序号
print(str[-1])

# 字符切片
print(str[1:2]) # 从第二个字符到第二个字符
print(str[2:-1]) # 从第二个字符到倒数第二个字符
print(str[2:]) # 从第二个字符到最后一个字符
print(str[:4]) # 第一个序号缺失表示至开头
print(str[:]) # 第二个序号缺失表示至结尾

# 根据步长对字符串切片
print(str[1:8:3])
print(str[::3])

# 转义符\
print("这里有个双引号(\")")
print("这里有个单引号(\')")
print("这里有个转义符反斜杆(\\)")

print("转义符(\\b)表示回退(删除最后一个字符）")
print("转义符(\\n)表示光标移动到下行首")
print("转义符(\\r)表示光标移动到本行首")

# 字符串操作符
x = '123'
y = '一二三'
print(x + y)
print(3 * x)
print(y * 4)
print(x in y)
print('12' in x)