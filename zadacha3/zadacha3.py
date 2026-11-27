alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
couples = [letter1 + letter2 for letter1 in alphabet for letter2 in alphabet]
# for i, l in enumerate(pares):
#    print(l)


def chastota_par(text):

    col_of_couples = [text.count(a) for a in couples]
    total_couples = len(text) - 1
    frequency_of_couples = [round(col / total_couples, 4) for col in col_of_couples]
    return frequency_of_couples


with open("text1.txt") as text1:
    frequancy_text1 = chastota_par(text1.read().lower())
with open("text2.txt") as text2:
    frequancy_text2 = chastota_par(text2.read().lower())

for i, l in enumerate(couples):
    print(l, frequancy_text1[i], frequancy_text2[i])
