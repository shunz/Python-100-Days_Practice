'''
定义和使用时钟类
'''

import time
import os

class Clock(object):

    # Python中的函数没有重载的概念
    # 因为Python中函数的参数没有类型，而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重构

    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return f'{self._hour:02}:{self._minute:02}:{self._second:02}'


if __name__ == '__main__':
    # clock = Clock(hour=10, minute=5, secon=58)
    clock = Clock()
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()
