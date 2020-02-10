'''
去掉字符串最后一个逗号分隔符的方法：

'''

strs = '1,2,3,4,5,'
print(strs)

# 1. 用str[:-1]切片
print(strs[:-1])

# 2. 用str.rstrip(',')删除尾部的字符
print(strs.rstrip(','))

# 3. 还可以用if str.endswith(',')判断,然后删除
if strs.endswith(','):
    print(strs[:-1])

# 4. 放入列表，然后 ','.join(list)
s = []
for i in range(1,6):
    s.append(str(i))

print(','.join(s))
    
