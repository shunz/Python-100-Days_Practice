'''
练习1：在屏幕上显示跑马灯文字 
'''

import os
import time

def main():
    content = '北京欢迎你，为你开天辟地…………'
    while True:
        # 清理屏幕上的输出(IDLE上不支持清屏)
        os.system('clear')
        # cls()
        print(content)
        # 休眠 200 毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

def cls():
    # 刷100行，模拟清屏
    print('\n' * 100)

if __name__ == '__main__':
    main()
