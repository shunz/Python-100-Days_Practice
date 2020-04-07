"""3.2 天天向上续1"""

dayup = 1
factor = 0.01
for i in range(1,366):
    if i % 7 in [4, 5, 6, 0]:
        dayup *= 1 + factor
print(f'{dayup:.2f}')
