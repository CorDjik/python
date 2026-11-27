import random
import time


def have_neighbor(pole, x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or i >= len(pole):
                continue
            if j < 0 or j >= len(pole[0]):
                continue
            if pole[i][j] == 1:
                count += 1
    return count


def new_pole_generate(pole):
    pole_ = [[0 for i in range(100)] for j in range(50)]
    for i in range(len(pole)):
        for j in range(len(pole[0])):
            n = have_neighbor(pole, i, j)
            if pole[i][j] == 1 and (n == 2 or n == 3):
                pole_[i][j] = 1
            if pole[i][j] == 0 and n == 3:
                pole_[i][j] = 1
    return pole_


pole = [[1 if random.random() < 0.25 else 0 for i in range(100)] for j in range(50)]

while True:
    new_pole = [
        [" " if pole[j][i] == 0 else "*" for i in range(100)] for j in range(50)
    ]
    for i in new_pole:
        print(" ".join(i))
    # a = input("Press Enter")
    time.sleep(0.1)
    pole = new_pole_generate(pole)
