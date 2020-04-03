"""乒乓选手雷达图绘制"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='Arial Unicode MS'
matplotlib.rcParams['font.sans-serif']=['Arial Unicode MS']

radar_labels = np.array(['爆发力','技巧熟练度','气势',\
                         '稳定性','速度'])
nAttr = 5
data = np.array([[0.8,0.9,0.9,0.75],
                 [0.85,0.87,0.9,0.9],
                 [0.9,0.6,1.0,0.6],
                 [0.8,0.7,0.7,0.9],
                 [0.6,0.9,0.9,0.92]]
                )
data_labels = ('马龙','张继科','马琳',\
               '王励勤')
angles = np.linspace(0, 2*np.pi, nAttr, endpoint = False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor = 'white')
plt.subplot(111, polar = True)
plt.plot(angles, data, 'o-', linewidth = 1.5, alpha = 0.9)
plt.fill(angles, data, alpha = 0.2)
plt.thetagrids(angles*180/np.pi, radar_labels)
plt.figtext(0.05, 0.97, '中国国家队乒乓球运动员参数雷达图',ha =
            'left', size = 15)
legend = plt.legend(data_labels, loc = (0.9,0.92), labelspacing= 0.1)
#plt.setp(legend.get_texts(), fontsize = 'small')
#plt.grid(True)
plt.savefig('9.5PingPong_holland_radar.jpg')
plt.show()
