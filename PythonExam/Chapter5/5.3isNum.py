"""实现isNum()函数

参数为一个字符串，如果这个字符串属于整数、浮点数或复数的表示，则返回True，否则返回False

python中合法的数字有十进制整数，浮点数，十六进制整数，复数
"""

def isNum(num):
    np = '+-'
    numbers = '.0123456789'
    numbersE = '.0123456789+-jJeE'
    x16 = '0123456789abcdefABCDEF'

    if num[0] in np:
        try:
            return isNum(num[1:])
        except:
            return False

    elif num[0] in numbers:
        if num[:2] == '0x':
            for i in num[2:]:
                if i not in x16:
                    return False
            return True
        else:
            ele = 0
            point = 0
            last = ''
            numaftere = 0
            q = 0
            for i in num:
                q += 1
                if i not in numbersE:
                    return False
                else:
                    if point == 0 and i == '.':
                        point = 1
                        continue
                    if point == 1 and (numaftere == 1 or ele == 0) and i in '+-':  # 一个数字结束，进入了第二个数字(一般是复数)
                        point = 0
                        continue
                    if ele == 0 and i in 'Ee':  # 出现了第一个E，一个浮点数中只能出现一个E
                        ele = 1
                        continue
                    if ele == 1 and i in '0123456789':
                        numaftere = 1
                        continue
                    if ele == 1 and numaftere == 1 and i in '+-':  # 针对复数的特例
                        ele = 0
                        numaftere = 0
                        continue
                    if last == '.' and i in '+-':
                        return False
                    elif (point == 1 or last in 'EeJj') and i == '.':
                        return False
                    elif i in 'Jj' and last in '+-':
                        return False
                    elif ele == 1 and i in 'Ee.':
                        return False
                last = i
            if last == '.' and i in '+-':
                return False
            elif (point == 1 or last in 'EeJj') and i == '.':
                return False
            elif i in 'Jj' and last in '+-.':
                return False
            elif ele == 1 and i in 'Ee.':
                return False
            else:
                return True
    else:
        return False


print(isNum('Hello'))
print(isNum('+++++++++++++++++++++++++++++++++++++'))
print(isNum('+-+-+-+-+-+-3'))
print(isNum('100'))
print(isNum('10e10'))
print(isNum('10e+10'))
print(isNum('10e10.'))
print(isNum('10e10e'))
print(isNum('10e10+4E10'))
print(isNum('10e'))
print(isNum('10e+1j'))
print(isNum('10e10+1.j'))
print(isNum('1.0e+10-j'))
print(isNum('1.0e+1j-3.e'))
print(isNum('1.0e10+1j-3.e10'))
print(isNum('1.3333'))
print(isNum('.3333'))
print(isNum('.333.3'))
print(isNum('.3333e5'))
print(isNum('12345678'))
print(isNum('0abddf'))
print(isNum('0xabddf'))
