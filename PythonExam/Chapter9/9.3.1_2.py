"""将图像读入ndarray数组对象后，可以通过任意数学操作来获取相应的图像变换。
以灰度变换为例，分别对灰度变化后的图像进行反变换、区间变换和像素值平方处理。
需要注意的是，有些数学变换后会改变图像的数据类型，所以在重新生成PIL图像前
要先将数据类型通过numpy.uint()变换成整数
"""

from PIL import Image
import numpy as np
img0 = np.array(Image.open('./pics/sample.jpg').convert('L'))
img1 = 255 - img0  # 反变换
img2 = (100/255)*img0 + 150  #区间变换
img3 = 255*(img1/255)**2  # 像素平方处理

pil_img = Image.fromarray(np.uint(img1))
pil_img.show()
