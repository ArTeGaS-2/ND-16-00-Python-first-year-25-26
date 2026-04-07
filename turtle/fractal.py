import turtle as t # Імпортуємо у файл і скорочуємо до "t"

draw_distance = 10 # Довжина лінії
angle = 91 # Кут обертання
repeat_num = 999999 # Кількість ітерацій циклу
current_iter = 0 # Поточна ітерація

colors = [
    "red",
    "orange", 
    "yellow", 
    "green",
    "blue",
    "purple"]

# Налаштування пера
t.title("Квадрат") # Заголовко вікна
t.speed(0) # Швидкість руху пера
t.pensize(3) # Розмір пера

# Малюємо квадрать 100x100 пікселів
for _ in range(repeat_num):
    t.color(colors[current_iter]) # Обираємо колір

    t.forward(draw_distance) # Рух вперед у пікселях
    t.left(angle) # Поворот у градусах
    draw_distance += 1
    if current_iter < len(colors) - 1:
        current_iter += 1
    else:
        current_iter = 0

t.done()