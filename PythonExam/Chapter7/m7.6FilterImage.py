"""图像的轮廓获取"""

from PIL import Image as I
from PIL import ImageFilter as F
img = I.open('./pics/sample2.jpg')

contour = img.filter(F.CONTOUR)
contour.save('./pics/sample2_Contour.jpg')

blur = img.filter(F.BLUR)
blur.save('./pics/sample2_Blur.jpg')

Detail = img.filter(F.DETAIL)
Detail.save('./pics/sample2_Detail.jpg')

Edge = img.filter(F.EDGE_ENHANCE)
Edge.save('./pics/sample2_Edge.jpg')

EdgeMore = img.filter(F.EDGE_ENHANCE_MORE)
EdgeMore.save('./pics/sample2_EdgeMore.jpg')

EMBOSS = img.filter(F.EMBOSS)
EMBOSS.save('./pics/sample2_EMBOSS.jpg')

FIND_EDGES = img.filter(F.FIND_EDGES)
FIND_EDGES.save('./pics/sample2_FIND_EDGES.jpg')

SMOOTH = img.filter(F.SMOOTH)
SMOOTH.save('./pics/sample2_SMOOTH.jpg')

SMOOTH_MORE = img.filter(F.SMOOTH_MORE)
SMOOTH_MORE.save('./pics/sample2_SMOOTH_MORE.jpg')

SHARPEN = img.filter(F.SHARPEN)
SHARPEN.save('./pics/sample2_SHARPEN.jpg')
