"""图像是有规则的二维数据，可以用numpy库将图像转换成数组对象

- 图像转换对应的ndarray类型是三维数据，如(1080, 1000, 3)
    - 其中前两维表示图像的长度和宽度，单位是像素
    - 第三维表示每个像素点的GRB值，每个RGB值是一个单字节整数
"""

from PIL import Image
import numpy as np

for i in ['','2','3','5']:
    img = np.array(Image.open('../Chapter7/pics/sample'+i+'.jpg'))
    print(img.shape, img.dtype)

"""
PIL库包括图像转换函数，能够改变图像单个像素的表示形式，使用convert()函数，
这是'L'模式，表示将像素从RGB的3字节形式转变为单一数值形式，数值范围为0~255，
表示灰度色彩变化。此时，图像从彩色变为带有灰度的黑白色。转换后，图像的ndarray
类型变为二维数据，每个像素点色彩只由一个整数表示
"""
img = np.array(Image.open('./pics/sample.jpg').convert('L'))
print(img.shape, img.dtype)

