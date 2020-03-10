"""用PIL去掉图像中的红色通道

- 输入
    - 打开测试图像文件
- 处理
    - 将图像分解为rgb三个通道
    - 对红色通道进行编辑，使其所有颜色值变为0
    - 将三个通道重新合并
- 输出
    - 保存输出合并的图像文件
"""

from PIL import Image as I

img = I.open('./pics/sample2.jpg')

r, g, b = img.split()
removeR = r.point(lambda x: 0)  # 将R通道颜色值变为0
removeG = g.point(lambda x: 0)  # 将G通道颜色值变为0
removeB = b.point(lambda x: 0)  # 将B通道颜色值变为0

removeR = I.merge(img.mode, (removeR, g, b))  
removeR.save('./pics/sample2_exchanged_removeR.jpg')

removeG = I.merge(img.mode, (r, removeG, b))  
removeG.save('./pics/sample2_exchanged_removeG.jpg')

removeB = I.merge(img.mode, (r, g, removeB)) 
removeB.save('./pics/sample2_exchanged_removeB.jpg')
