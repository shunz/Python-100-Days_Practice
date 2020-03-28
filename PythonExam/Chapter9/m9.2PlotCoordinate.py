"""带标签的坐标系"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='Arial Unicode MS'
matplotlib.rcParams['font.sans-serif']=['Arial Unicode MS']
plt.plot([1,2,4],[1,2,3])
plt.title('坐标系标题')
plt.xlabel('时间(s)')
plt.ylabel('范围(m)')
plt.xticks([1,2,3,4,5],[r'$\pi/3$', r'$2\pi/3$', r'$\pi$', \
                        r'$4\pi/3$', r'$5\pi/3$'])
plt.show()


# 如下代码可以查看系统可用字体
from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)
