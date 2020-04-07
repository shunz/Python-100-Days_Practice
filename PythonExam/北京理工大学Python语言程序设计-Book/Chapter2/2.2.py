"""程序练习题 2.2 汇率兑换程序

按照1美元=7人民币汇率编写一个美元和人民币的双向兑换程序
"""

try:
    while 1: 
        money = input('请输入需要兑换的金额，比如：￥235, $128, e退出：')
        mode = money[0]
        if mode == '￥':
            print(f'{money}可兑换${eval(money[1:])/7.1:.2f}')
        elif mode == '$':
            print(f'{money}可兑换￥{eval(money[1:])*7.1:.2f}')
        elif mode == 'e':
            break
        else:
            print('Oops, 输入有误')

except:
    print('输入有误')


