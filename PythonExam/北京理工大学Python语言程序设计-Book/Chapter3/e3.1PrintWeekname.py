weekstr='星期一星期二星期三星期四星期五星期六星期日'
while 1:
    weekid = input('请输入星期数字(1-7), q for quit：')
    if weekid == 'q':
        break
    elif eval(weekid) in range(1,8):
        pos = (eval(weekid) - 1) * 3
        print(weekstr[pos: pos+3])
    else:
        print('输入格式不对哟')
    
