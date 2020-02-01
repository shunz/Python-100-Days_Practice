import practice02 as p02
import practice03 as p03

if __name__ == '__main__':
    while True:
        num = int(input('请输入回文素数：'))
        if p02.is_palindrome(num) and p03.is_prim(num):
            print('%d是一个回文素数' % num)
