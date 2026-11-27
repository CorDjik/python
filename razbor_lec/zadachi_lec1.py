# задача2
a = 3726

hour = a // 3600
minunts = (a % 3600) // 60
seconds = a % 60

print(f"{hour}часа {minunts}минут {seconds}секунд")

# задача3
import math

print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))

# задача4
s = "программирование"
print(s[:3], s[-3:], s[::2], s[::-1])

# задача5


# задача6
name = "Кабирова Алия Рашидовна"
first_name = name.split()

print(f"{first_name[0]} {first_name[1][0]}. {first_name[2][0]}.")

# задача7
a = "уеыаоэяию"
word = "я хочу кашать"
print(sum(1 for b in word if b in a))
# задача8
print([x**2 for x in range(2, 21, 2)])
# задача9
# не хочу
# задача10
g = (x**3 for x in range(1, 4))
print(next(g), next(g), next(g))
