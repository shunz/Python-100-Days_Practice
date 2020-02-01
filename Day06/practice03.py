'''
练习3：实现判断一个书是不是素数的函数
'''

def is_prim(num):
    '''判断一个数是不是素数'''
    divlist = []
    for factor in range(2, num):
        if num % factor == 0:
            divlist.append(factor)
            return False, divlist
    return True if num != 1 else False, divlist

if __name__ == '__main__':
    while True:
        num = int(input('请输入一个素数：'))
        if is_prim(num)[0]:
            print('%d是一个素数' % num)
        else:
            print('{}不是素数,能被{}整除'.format(num, is_prim(num)[1]))
