"""猜数字"""

from random import randint

num = randint(1, 10)
time = 0

while 1:
    try:
        guess = eval(input('请输入你猜的数字：'))
        time += 1
        if guess > num:
            print('遗憾，太大了')
        elif guess < num:
            print('遗憾，太小了')
        else:
            print(f'预测{time}次，你猜中了！')
            break
    except:
        print('输入有误')
    else:
        print('厉害了，就知道你很棒！')
    finally:
        print('加油⛽️')
