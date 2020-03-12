"""图像文件压缩

使用PIL库对图片进行等比压缩，无论压缩前文件大小如何，压缩后文件小于10KB

- 输入
    - 打开一个图片文件
- 处理
    - 希望通过设置压缩参数中输出文件大小上限为10KB(but PIL的Image类似乎没有直接限制存储大小的参数)
    - 实际通过换算10k大小与图片大小之间的比值来折算压缩后的长宽尺寸大小
        - 通过os库的stat()方法获得图片存储大小
- 输出
    - 覆盖原图片或保存为新的图片
"""

from PIL import Image as I
import os

def getsize(path):  # 获取图片文件的存储大小
    return os.stat(path).st_size  # 用os库的stat()方法获取

def compress(path):
    img = I.open(path)
    size = getsize(path)
    # 10k和当前图片大小的比值的开方，需要开方是因为这个比值是整个图片大小面积的，而面积=长*宽，so分解到长和宽上就需要开方
    ratio = (10 * 1024 / size) ** 0.5  
    print(ratio)
    width = int(img.width * ratio)
    height = int(img.height * ratio)
    m_img = img.resize((width, height))
    m_img.save(f'{path[:-4]}_10k{path[-4:]}')  # 在原图片名后增加一个后缀
    #m_img.save(f"{path[:(path.rfind('.')-len(path))]}_10k{path[(path.rfind('.')-len(path)):]}")

compress('../pics/sample5.jpg')
# 实测压缩后会比10k大，原图尺寸越大，差别越大，所以这个算法思路不够精准
