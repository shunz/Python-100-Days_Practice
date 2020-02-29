"""3.1 重量计算

月球上物体的体重是在地球上的16.5%，加入你在地球上每年增长0.5kg，编写程序输出未来10年你在地球和月球上的体重状况。
"""

weight = eval(input('请输入你的体重(kg数)：'))
wei10ear = weight + 0.5 * 10
wei10moo = wei10ear * 0.165
print(f'10年后你在地球上的体重是{wei10ear:.2f}kg, 在月球上的体重是{wei10moo:.2f}kg')
