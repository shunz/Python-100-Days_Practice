'''
打印三角形图案

Ver: 0.1
Author: Shunz
Last_update: 2020-01-11
'''

n = int(input('三角形层数：'))
for i in range(n):
    for _ in range(i+1):
        print('*', end='')
    print()

print()


for i in range(n):
    print(' '*(n-i-1),end='')
    for _ in range(i+1):
        print('*',end='')
    print()

print()


for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

print()


for i in range(n):
    print(' '*(n-i-1),end='')
    for _ in range((i+1)*2-1):
        print('*',end='')
    print()

print()

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for _ in range(2*i+1):
        print('*', end='')

    print()
