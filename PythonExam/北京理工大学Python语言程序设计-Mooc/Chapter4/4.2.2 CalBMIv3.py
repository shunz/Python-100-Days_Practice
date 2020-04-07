# CalBMIv3.py
# 身体质量指数 BMI
'''
height, weight = eval(input('请输入身高（米）和体重（公斤），逗号隔开：'))
bmi = weight / pow(height, 2)
print('BMI 数值为：{:.2f}'.format(bmi))
who = local = ''
if bmi < 18.5:
    who = local = '偏瘦'
elif 18.5 < bmi < 24:
    who = local = '正常'
elif 24 < bmi < 25:
    who = '正常'
    local = '偏胖'
elif 25 < bmi < 28:
    who = local = '肥胖'  
elif 28 < bmi < 30:
    who = '偏胖'
    local = '肥胖'
else:
    who = '肥胖'
print('BMI 指标为：国内"{}"，国际"{}"'.format(who,local))
'''


height, weight = eval(input('请输入身高（米）和体重（公斤），逗号隔开：'))
bmi = weight / pow(height, 2)
print('BMI 数值为：{:.2f}'.format(bmi))
who,local = '',''
if bmi < 18.5:
    who,local = '偏瘦','偏瘦'
elif 18.5 < bmi < 24:
    who,local = '正常','正常'
elif 24 < bmi < 25:
    who,local = '正常','偏胖'
elif 25 < bmi < 28:
    who,local = '偏胖','偏胖'  
elif 28 < bmi < 30:
    who,local = '偏胖','肥胖'
else:
    who,local = '肥胖','肥胖'
print('BMI 指标为：国内"{}"，国际"{}"'.format(who,local))
