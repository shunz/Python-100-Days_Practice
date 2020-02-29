"""3.6 StartingDone"""

from time import sleep
print('Starting', end='')
for i in range(10):
    print(chr(8901), end= '')
    sleep(0.5)
print('Done!')
