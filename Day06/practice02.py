'''
练习2：实现判断一个数是不是回文数的函数
'''

'''
def is_palindrome(num):
    #判断一个数是不是回文数

    # 将数字转换为字符，用切片取反，再转为数字，然后判断取反的数是否与原数相同
    reve_num = int(str(num)[::-1])
    if reve_num == num:
        return reve_num
    
if __name__ == '__main__':
    while True:
        x = eval(input('请输入一个数字 = '))
        if not isinstance(x, int):
            print('输入的不是一个数字')
        elif is_palindrome(x) == None:
            print('%d不是一个回文数' % x)
        else:
            print('%d是一个回文数' % x)
'''        

def is_palindrome(num):
    # 判断一个数是不是回文数

    temp = num
    total = 0
    while temp > 0:
        # 将当前临时数按10模运算取其个位数，加上上一步求得的取反数乘10(也就是不断取出当前临时数的个位数，重新拼成取反数)
        total = total * 10 + temp % 10
        # 临时数整除10,降一个数量级，进入下一个循环继续按10模运算取其个位数
        temp //= 10
    return total == num
    
if __name__ == '__main__':
    while True:
        x = eval(input('请输入一个数字 = '))
        if is_palindrome(x):
            print('%d是一个回文数' % x)
        else:
            print('%d不是一个回文数' % x)
        
