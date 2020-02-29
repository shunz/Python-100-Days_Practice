# 函数递归实例解析

# Example 1. 字符串反转
def rvs(s):
    if s == '':
        return ''
    else: # 递归链条很重要的点是当前操作和之前的一步之间的关系，通过将首字符放到其余字符的后面，并继续将其余字符再反转
        return rvs(s[1:])+s[0]

print(rvs('abcdefghijklmn'))

# Example 2. 斐波那契数列
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(10))

# Example 3. 汉诺塔问题
count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1,src,dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst) # 第一步，将n-1个圆盘先一起整体考虑从源柱子搬到中间柱子，搬运过程中，使用目标柱子作为过渡
        print('{}:{}->{}'.format(n,src,dst)) # 第二步，将第n号圆盘从源柱子移动到目标柱子
        count += 1
        hanoi(n-1, mid, dst, src) # 第步，将n-1个圆盘一起整体考虑从中间柱子搬到目标柱子，源柱子作为过渡

hanoi(10, 'A', 'C', 'B')
print(count)