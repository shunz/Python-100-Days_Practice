"""GIF文件图像提取

对一个GIF格式动态文件，提取其中各帧图像，并保存为文件
"""

from PIL import Image as I
img = I.open('./pics/alpacas.gif')
try:
    img.save(f'./pics/alpaca{img.tell():02d}.png')
    while 1:
        img.seek(img.tell() + 1)
        img.save(f'./pics/alpaca{img.tell():02d}.png')
except:
    print('处理结束')
img.thumbnail((128, 128))
img.save('./pics/thumbnail.png', 'png')

img2 = img.resize((200, 200))
img2.save('./pics/resized.png')

img3 = img.rotated(180)
img3.save('./pics/rotated.png')
