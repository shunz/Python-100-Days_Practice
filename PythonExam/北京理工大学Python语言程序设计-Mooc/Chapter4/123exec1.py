# 实例5：身体质量指数BMI


height,weight = eval(input())
bmi = weight / (height ** 2)
print('BMI数值为:{:.2f}'.format(bmi))

if bmi < 18.5:
    g = l = '偏瘦'
elif 18.5 <= bmi < 24:
    g = l = '正常'
elif 24 <= bmi < 25:
    g,l = '正常','偏胖'
elif 25 <= bmi < 28:
    g = l = '偏胖'
elif 28 <= bmi < 30:
    g,l = '偏胖','肥胖'
else:
    g = l = '肥胖'
    
print("BMI指标为:国际'{}',国内'{}'".format(g,l))