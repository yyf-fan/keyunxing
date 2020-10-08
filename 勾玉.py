import turtle
mp = turtle.Pen()
mp.speed(0)

#放置图案居中
mp.penup()
mp.goto(140,86)
mp.pendown()

#for循环绘制勾玉
for j in range(3):
    #双曲线绘制勾
    mp.fillcolor("black")
    mp.begin_fill()
    mp.dot(100,"black")
    mp.backward(50)
    mp.right(90)
    mp.circle(100,-90)
    mp.circle(50,150)
    mp.end_fill()
    #计算转向时考虑画笔方向
    mp.right(90)
    mp.penup()
    mp.forward(300)
    mp.pendown()


turtle.done()