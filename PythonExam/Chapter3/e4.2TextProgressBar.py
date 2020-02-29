import time
for i in range(101):
    print(f'\r{i:2}%', end='')
    time.sleep(0.02)
