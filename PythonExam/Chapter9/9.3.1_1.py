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
