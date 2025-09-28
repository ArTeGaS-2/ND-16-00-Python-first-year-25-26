import turtle as t

t.title("Заняття 1 - базовий квадрат") # Заголовок
t.speed(5) # Швидкість
t.pensize(3) # Розмір пера
t.color("black")

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup; t.goto(0,100); t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.done()