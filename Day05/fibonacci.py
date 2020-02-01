'''
生成斐波拉契数列的前20个数

斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
'''

'''
first = second = 1
print(first,second, end=',')
for _ in range(18):
    sum2 = first + second
    print(sum2, end=',')
    first = second
    second = sum2

'''

first = 0
second = 1
for _ in range(20):
    first, second = second, first + second
    print(first, end=',')

