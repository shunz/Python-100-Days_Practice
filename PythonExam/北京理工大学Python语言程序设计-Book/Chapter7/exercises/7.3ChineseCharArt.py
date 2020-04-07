"""中文字符画

编写程序合理选取中文字符构造字符表，生成中文字符画
"""

from PIL import Image as I
unicode_char = list('　一卜二三人大个六七八九十水火五中文取造理编测赢蕾')

def get_char(r,g,b, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = 256/len(unicode_char)

    return unicode_char[int(gray // unit)]

def main(filename):
    img = I.open(filename)
    WIDTH, HEIGHT = 100,72
    img = img.resize((WIDTH, HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*img.getpixel((j, i)))
        txt += '\n'
    fo = open(filename[filename.rfind('/')+1:] + '_pic.txt', 'w')
    fo.write(txt)
    fo.close()

main('../pics/sample5.jpg')
