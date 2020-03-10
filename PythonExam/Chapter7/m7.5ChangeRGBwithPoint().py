"""图像的颜色交换

采用lamba函数和point()方法操作图像的每个像素点
"""

from PIL import Image as I
img = I.open('./pics/sample2.jpg')
r, g, b = img.split()
newg = g.point(lambda x: x*0.9)  # 将G通道颜色值变为原来的0.9倍
newb = b.point(lambda x: x<100)  # 选择B通道值低于100的像素点
imgExchange = I.merge(img.mode, (r, newg, newb))  # 将3个通道合成为新图像
imgExchange.save('./pics/sample2_exchanged_point().jpg')
