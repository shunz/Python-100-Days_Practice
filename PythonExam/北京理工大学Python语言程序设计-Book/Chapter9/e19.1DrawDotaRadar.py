"""绘制DOTA人物能力值雷达图"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Arial Unicode MS'
matplotlib.rcParams['font.sans-serif']=['Arial Unicode MS']
labels = np.array(['综合','KDA','发育','推进','生存','输出'])
nAttr = 6
data = np.array([7,5,6,9,8,7])  # 数据值
angles = np.linspace(0, 2*np.pi, nAttr, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor='white')
plt.subplot(111, polar=True)
plt.plot(angles, data, 'bo-', color='r', linewidth=2)
plt.fill(angles, data, facecolor='r', alpha=0.25)
plt.thetagrids(angles*180/np.pi, labels)
plt.figtext(0.52, 0.95, 'DOTA能力值雷达图', ha='center')
plt.grid(True)
plt.savefig('e19.1_dota_radar.jpg')
plt.show()
