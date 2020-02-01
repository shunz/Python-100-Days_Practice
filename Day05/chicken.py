'''
百鸡百钱问题

'''

for roosters in range(0,20):
    for hens in range(0,33):
        chicks  = 100 - roosters - hens
        if roosters * 5 + hens * 3 + chicks / 3 == 100:
            print('公鸡：%d只，母鸡：%d只，小鸡：%d只' % (roosters, hens, chicks))
