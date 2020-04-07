"""带局部阴影的坐标系"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.cos(2 * np.pi * x) * np.exp(-x) + 0.8
plt.plot(x, y, 'k', color='r', linewidth=3, label='$exp-decay$')
plt.axis([0,6,0,1.8])
ix = (x>0.8) & (x<3)
plt.fill_between(x, y, 0, where = ix, \
                 facecolor='tomato', alpha=0.25)
plt.text(0.5*(0.8+3), 0.2, r'$\int_a^b f(x)\mathrm{d}x$', \
         horizontalalignment='center')
plt.legend()
plt.show()

