#我的casio屏幕
import turtle as t
import time 
t.speed(10)
t.pensize(10)
t.setup(800,800,0,0)
t.pu()
t.goto(-300,0)
t.pd()

def soth():
    t.pu()
    t.pd()
    t.fd(100)

def drawline(now):
    t.pu()
    soth() if now in [2,3,4,5,6,8,9] else t.fd(100)
    t.right(90),t.pu()
    soth() if now in [0,1,3,4,5,6,7,8,9] else t.fd(100)
    t.right(90),t.pu()
    soth() if now in [0,2,3,5,6,8,9] else t.fd(100)
    t.right(90),t.pu()
    soth() if now in [0,2,6,8] else t.fd(100)
    t.left(90)
    t.right(90),t.pu()
    soth()if now in [0,4,5,6,8,9] else t.fd(100)
    t.right(90),t.pu()
    soth() if now in [0,2,3,5,6,7,8,9] else t.fd(100)
    t.right(90),t.pu()
    soth() if now in [0,1,2,3,4,7,8,9] else t.fd(100)

print(time.gmtime())
settime = time.gmtime()
hour  = [int((settime[3]+8)/10),(settime[3]+8)%10]
minu = [int(settime[4]/10),settime[4]%10]
print(hour,minu)

def draw_draw():
    for i in range(2):
        drawline(hour[i])
        t.pu()
        t.left(90)
        t.forward(50)
    for i in range(2):
        drawline(minu[i])
        t.pu()
        t.left(90)
        t.forward(50)
draw_draw()
t.done()