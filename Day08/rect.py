'''
定义和使用矩形类
'''

class Rect(object):
    '''矩形类'''

    def __init__(self, width=0, height=0):
        '''初始化方法'''
        self.__width = width
        self.__height = height

    def perimeter(self):
        '''计算周长'''
        return (self.__width + self.__height) * 2

    def area(self):
        '''计算面积'''
        return self.__width * self.__height

    def __str__(self): # 返回对象的描述信息(一个字符串)，当print对象时，打印从本方法return的数据
        '''矩形对象的字符串表达式'''
        return f'矩形[{self.__width},{self.__height}]'

    def __del__(self):
        '''析构器'''
        print('销毁矩形对象')


if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
    del(rect2)
