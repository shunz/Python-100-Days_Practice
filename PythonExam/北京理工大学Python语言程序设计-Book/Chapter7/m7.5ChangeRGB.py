"""图像的颜色交换"""

from PIL import Image as I
img = I.open('./pics/sample2.jpg')
r, g, b = img.split()
imgExchange = I.merge('RGB', (g, b, r))
imgExchange.save('./pics/sample2_exchanged_gbr.jpg')
