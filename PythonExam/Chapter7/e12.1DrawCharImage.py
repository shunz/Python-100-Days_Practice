"""DrawCharImage

- 输入
    - 一个图像文件
- 处理
    - 自定一个字符集，用来替代图像中的像素点，使每个字符对应图像中的不同颜色
        - 不同字符的视觉效果不同，@#&$这类字符有浓密的色彩感，适合表示深色，而`.!/-这类字符空白较多，适合表示浅色
        - 可在生成字符画后，对照字符集适当修改字符排列顺序
    - 用灰度值将彩色图像转换为高质量的黑白图像
        - 白色为255，黑色为0
        - 定义灰度值从小到大使用字符集中从左到右的字符，可求出不同灰度值对应字符集中的字符编号
        - 定义彩色向灰度转换的公式
            - Gray = R * 0.2126 + G * 0.7152 + B * 0.0722
    - 重新设定图像大小
    - 逐行打印对应像素点的字符到字符串变量中
- 输出
    - 保存字符串到一个文本文件中
"""

from PIL import Image as I

#ascii_char = [chr(i) for i in range(32, 127)]
#ascii_char = list("#$%&@*ABCDEFGHJKMNOPQRSTUVWXYZIL0123456789?abcdefghijklmnopqrstuvwxyz[]\'()\\/<>:;+=-^_,.`")
ascii_char = list(" .,_`'^-=+;:></\\)(][zyxwvutsrqponmlkjihgfedcba?9876543210LIZYXWVUTSRQPONMKJHGFEDCBA*@&%$#")

def get_char(rgb, alpha=256):
    if alpha == 0:
        return ' '
    #gray = int(rgb[0]*0.2126 + rgb[1]*0.7152 + rgb[2]*0.0722)
    gray = int(rgb[0]*0.299 + rgb[1]*0.587 + rgb[2]*0.114)
    return ascii_char[int(gray/256 * len(ascii_char))]

#print(get_char(255,255,255))

def main():
    img = I.open('./pics/sample5.jpg')
    WIDTH, HEIGHT = 200, 108
    imgRs = img.resize((WIDTH, HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(imgRs.getpixel((j, i)))  # img.getpixel()方法返回给定图像位置(j,i)坐标的像素值，若是多通道图像，返回一个RGB颜色元组
        txt += '\n'
    fo = open('e12.1DrawCharImage4.txt', 'w')
    fo.write(txt)
    fo.close()

main()
