# 星号三角形

# Algorithm 1
'''
n = eval(input())
if n % 2 == 1:
    for i in range(n):
        if (i + 1) % 2 ==1:
            star = '*' * (i+1)
            print(star.center(n))
else:
    print('你输入的是偶数')
'''

# Algorithm 2
n = eval(input())
for i in range(1,n+1,2):
    star = '*' * i
    print(star.center(n))
    
    # 另一种输出星号的方式，关键是.format()中槽可以嵌套槽，用来表示填充、宽度、浮点精度等
    # print('{0: ^{1}.{2}}'.format(1/3,n,i))
    