#open package
import turtle as tt
zakki = tt.Turtle()
zakki.speed(7)
zakki.color("black","black")
zakki.pensize(3)

#draw head

zakki.circle(100)

#draw right ear

zakki.penup()
zakki.setx(50)
zakki.sety(185)
zakki.pendown()
zakki.begin_fill()
zakki.right(90)
zakki.circle(30, -260)
zakki.end_fill()

#draw left ear

zakki.penup()
zakki.setx(-50)
zakki.sety(185)
zakki.pendown()

zakki.left(170)
zakki.begin_fill()
zakki.right(90)
zakki.circle(30, 260)
zakki.end_fill()

#draw left eye

zakki.penup()
zakki.setx(-45)
zakki.sety(100)
zakki.pendown()
zakki.begin_fill()
zakki.circle(25)
zakki.end_fill()

zakki.penup()
zakki.setx(-35)
zakki.sety(130)
zakki.pendown()
zakki.color("white")
zakki.begin_fill()
zakki.circle(7)
zakki.end_fill()

#draw right eyezakki.penup()

zakki.color("black")
zakki.penup()
zakki.setx(45)
zakki.sety(100)
zakki.pendown()
zakki.begin_fill()
zakki.circle(25)
zakki.end_fill()

zakki.penup()
zakki.setx(35)
zakki.sety(130)
zakki.pendown()
zakki.color("white")
zakki.begin_fill()
zakki.circle(7)
zakki.end_fill()


#draw mouth and nose

zakki.color("black")
zakki.penup()
zakki.setx(0)
zakki.sety(80)
zakki.pendown()
zakki.circle(7)

zakki.penup()
zakki.setx(0)
zakki.setheading(-90)
zakki.pendown()
zakki.forward(35)

zakki.penup()
zakki.setx(40)
zakki.sety(85)
zakki.pendown()
zakki.setheading(-270)
zakki.circle(40,-180)

tt.done()