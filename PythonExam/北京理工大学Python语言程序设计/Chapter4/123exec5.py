# 用户登录的三次机会

count = 1
while count <= 3:
    name = input()
    psd = input()
    if name == 'Kate' and psd == '666666':
        print('登录成功！')
        break
    elif count != 3:
        count += 1
    else:
        print('3次用户名或者密码均有误！退出程序。')
        break
        