# 3.12
for i in range(101, 111):
	dayup = 1
	for d in range(365):
		if d % 7 in range(1,5):
			dayup *= i/100
	print(dayup)
print()

# 3.13
for i in range(101, 111):
	dayup = 1
	for d in range(365):
		if d % 7 in range(1,6):
			dayup *= i/100
	print(dayup)
print()

# 3.14
for i in range(101, 111):
	dayup = 1
	for d in range(365):
		if d % 7 in range(1,7):
			dayup *= i/100
	print(dayup)
print()

# 3.15
for i in range(101, 111):
	dayup = 1
	for d in range(365):
		if d % 30 in range(10):
			dayup *= i/100
	print(dayup)	
