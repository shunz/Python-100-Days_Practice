"""3.3 天天向上续2"""

dayup = 1
factor = 0.01
for i in range(1,366):
    if i % 10 != 0:
        dayup *= 1 + factor
print(f'{dayup:.2f}')
