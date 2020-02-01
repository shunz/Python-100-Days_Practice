'''
找出所有水仙花数

Ver: 0.1
Auther: Shunz
'''

for num in range(1000,10000):
    sd = single_digits = num % 10
    td = ten_digits = num // 10 % 10
    hd = hundred_digits = num // 100 % 10
    thd = thunsand_digits = num // 1000
    if num == sd ** 4 + td ** 4 + hd ** 4 + thd ** 4:
        print(num)
    
