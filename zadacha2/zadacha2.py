text = open("text.txt").read().lower()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# col = [0] * len(alphabet)

# for letter1 in text:
#    i = 0
#    for letter2 in alphabet:
#        if letter1 == letter2:
#            col[i] = col[i] + 1
#        i = i + 1


# col = [0 for i in range(len(alphabet))]
col = [sum([1 for letter1 in text if letter1 == letter2]) for letter2 in alphabet]

for i, l in enumerate(alphabet):
    print(l, round(col[i] / sum(col), 4))
