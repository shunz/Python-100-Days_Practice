"""ImageEnhance类的图像增强和滤镜方法"""

from PIL import Image as I
from PIL import ImageEnhance as E

img = I.open('./pics/sample2.jpg')

contrast = E.Contrast(img)
contrast.enhance(20).save('./pics/sample_enhance_contrast.jpg')

color = E.Color(img)
color.enhance(2).save('./pics/sample_enhance_color.jpg')

brightness = E.Brightness(img)
brightness.enhance(2).save('./pics/sample_enhance_brightness.jpg')

sharpness = E.Sharpness(img)
sharpness.enhance(15).save('./pics/sample_enhance_sharpness.jpg')
