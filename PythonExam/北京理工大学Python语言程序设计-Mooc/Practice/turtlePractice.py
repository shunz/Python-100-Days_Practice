import turtle as t

r = 10
dr = 40
head = 90

for i in range(4):
    t.pendown()
    t.circle(r)
    r +=  dr
    t.pu()
    t.seth(-head)
    t.fd(dr)
    t.seth(0)
    
t.done()
