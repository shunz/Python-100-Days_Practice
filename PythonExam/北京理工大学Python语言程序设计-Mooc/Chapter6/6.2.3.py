# 序列类型通用操作符
'''
x in s
x not in s
s + t
s*n / n*s 复制n次
s[i] 索引
s[i:j]或s[i:j:k] 切片，返回i到j以k为步长的元素子序列
'''

ls = ['python',123,'.io']
print(ls[::-1]) #从后到前提取元素的子序列
s = 'python123'
print(s[::-1]) #字符串也是序列类型的一种扩展形式

# 序列类型通用函数和方法
'''
len(s)
min(s) 返回最小元素，需可比较
max(s)
s.index(x)或 s.index(x,i,j) 返回从i到j首次出现x的位置
'''
print(len(ls))
print(ls.index(123))
print(ls.index('.io',0,3))
print(max(s))