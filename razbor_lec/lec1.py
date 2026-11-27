import math

print(math.sqrt(16))

print(math.floor(-10 / 3))
# округляет всегда вверх

print(math.trunc(-10 / 3))
# отпрасывает дробную часть

print(math.isclose(1.1, 1.1))
print(math.isclose(1.1, 1.2))
# сравнение чисел типа float

import random

print(random.randint(1, 10))
# генерирует рандомные числа в заданном диапозоне

print(random.choice(["a", "b", "c"]))
# выбирает раномный символ из списка


# стороки
v = "viking"
print(v[0], v[-1], v[1:4])
# v g iki
print(v[:2], v[2:], v[::2], v[::-1])
# vi king vkn gnikiv срез[ [начало:конец) :шаг]

print("C:\\new\\test")
# игнорирует специальные знаки \n \t

name = "alla, artur, brian"
print(name.split(", "))
parts = name.split(", ")
print(";".join(parts))
print("spam".find("pa"))
# возвращает индекс где начинается или -1 если не нашел
print("spam".replace("pa", "PA"))
print(v.count("i"))
print("123".isdigit(), "abc".isalpha())
print(ord("a"), chr(97))
# таблица аски

name, age = "Monty", 25
print("%s, %d" % (name, age))
print(f"{name}, {age}")
print(f"{3.14159:.2f}")
# '3.14' — два знака после точки

names = ["alla", "artur", "brian"]
print([x[:2] for x in names if x[0] == "a"])
# списковое включение
# ['al', 'ar']

g = (x * x for x in range(3))
# генератор (не создает сразу список,а выдает элемент через next())
print(next(g), next(g), next(g))
# 0 1 4
next(g)
# ошибка StopIteration: элементы кончились
