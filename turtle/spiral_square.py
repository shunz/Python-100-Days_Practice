import turtle as t

# 画螺旋正方形
def auto(num, length):
    gap = length
    for _ in range(num):
        for _ in range(2):
            t.fd(length)
            t.left(90)
        length += gap

auto(40, 10)
