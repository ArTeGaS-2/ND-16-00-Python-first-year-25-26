import turtle as t

t.title("Файл 2") # Заголовок
t.speed(5) # Швидкість
t.penup(); t.goto(-280, 120); t.pendown()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in colors:
    t.color(i)
    t.pensize(5)
    t.forward(80)
    t.penup(); t.forward(10); t.pendown()

t.done()

