"""Результат: програма має вивести правильну категорію за балами."""

score = int(input("Введи бали: "))

if score >= 50:
    print("Склав")
elif score >= 90:
    print("Відмінно")
else:
    print("Не склав")

info = {"name": "Оля"}
print("Ім'я:", info["ім'я"])
