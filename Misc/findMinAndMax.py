# 使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
	max = 0
	min = 999
	for i in L:
		if i < min:
			min =i
		if i > max:
			max = i
	return (min, max)

print(findMinAndMax([7,1,3,9,5]))
