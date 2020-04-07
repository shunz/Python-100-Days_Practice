# TempConvert.py

temp = input('请输入需要转换的温度')

if temp[-1] in ['F','f']:
    C = (eval(temp[0:-1])-32) / 1.8
    print("华氏"+str(temp[0:-1])+"°等于：摄氏"+"{:.2f}".format(C)+"°")
elif temp[-1] in ['C','c']:
    F = eval(temp[0:-1]) * 1.8 + 32
    print("摄氏"+str(temp[0:-1])+"°等于：华氏"+"{:.2f}".format(F)+"°")
else:
    print("输入格式错误")