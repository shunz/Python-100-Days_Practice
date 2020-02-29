def prime(m):
    flag = 1
    if m == 1:
        flag = 0
    for i in range(2, int(pow(m, 0.5)) + 1):
        if m % i == 0:
            flag = 0
            break
    return flag
 
 
n = eval(input())
a = int(n)
a = a + 1 if a < n else a
result = []
count = 5
while count > 0:
    if prime(a):
        result.append(str(a))
        count = count - 1
    a = a + 1
print(','.join(result))