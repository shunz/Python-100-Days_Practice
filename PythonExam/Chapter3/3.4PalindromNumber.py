"""3.4 回文数"""

n = input()
new = ''
for i in n:
    new = i + new
    print(new)

if n == new:
    print(f'Yay, {n}是一个回文数')
else:
    print(f'Oops, {n}不是回文数')
