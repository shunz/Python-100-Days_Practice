# 循环控制保留字
# break 跳过整个循环
# continue 跳过单次循环

for c in 'Python':
    if c == 't':
        continue
    print(c, end='')

print('\n')
for c in 'Python':
    if c == 't':
        break
    print(c, end='')

print('\n')
s = 'Python'
while s != '':
    for c in s:
        print(c,end='')
    s = s[:-1]

print('\n')
s = 'Python'
while s != '':
    for c in s:
        if c == 't':
            break
        print(c, end='')
    s = s[:-1]

print('\n')
s = 'Python'
while s != '':
    for c in s:
        if c == 't':
            continue
        if c == 'o':
            break
        print(c, end='')
    s = s[:-1]

print('\n')
s = 'Python'
for c in s:
    if c == 't':
        continue
    print(c, end='')
else:
    print('\nNo break，正常退出')