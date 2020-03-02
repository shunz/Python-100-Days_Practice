"""统计不同字符个数

用户从键盘输入一行字符，编写一个程序，统计并输出其中英文字符、数字、空格和其他字符的个数
"""

try:
    s = input('请输入一行字符：')
    ls = sorted({i for i in s})
    space = 0
    alpha = 0
    chinese = 0
    num = 0
    other = 0
    
    for i in ls:
        print(f"{s.count(i)}个'{i}'")
        
    for i in s:
        #if i.isalpha():  # 中文也会返回True，坑
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            alpha += 1
        elif i == ' ':
            space += 1
        elif '0' <= i <= '9':
            num += 1
        elif u'\u4e00' <= i <= u'\u9fd0':  # u'\u4e00' is '一',u'\9fd0' is '鿐'
            chinese += 1
        else:
            other += 1
    print(f'输入的字符串中有{space}个空格，{num}个数字，{chinese}个中文字符，{alpha}个英文字符，{other}个其他字符')
        
except:
    print('Sth. wrong')
