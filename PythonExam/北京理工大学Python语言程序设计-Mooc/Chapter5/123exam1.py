# import random

# def genpwd(length):
#     pwd = random.randint(length)
#     return pwd

# length = eval(input())
# random.seed(17)
# for i in range(3):
#     print(genpwd(length))

import random
def genpwd(length):
	return random.randint(10**(length-1),10**length-1)
    
length = eval(input())    
random.seed(17)
for i in range(3):
	print(genpwd(length))