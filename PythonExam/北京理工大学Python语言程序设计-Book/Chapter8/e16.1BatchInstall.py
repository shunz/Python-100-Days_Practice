"""用pip批量安装Python库的方法"""

import os
'''libs = {'numpy', 'matplotlib', 'pillow','sklearn','requests',\
        'jieba', 'beautifulsoup4', 'wheel', 'networkx', 'sympy',\
        'pyinstaller', 'django', 'flask', 'werobot', 'pyqt5', \
        'pandas', 'pyopengl', 'pypdf2', 'docopt', 'pygame'}
'''
libs = {'jieba', 'flask'}

try:
    for lib in libs:
        os.system('pip3 install ' + lib)
    print('Successful')
except:
    print('Failed Somehow')
