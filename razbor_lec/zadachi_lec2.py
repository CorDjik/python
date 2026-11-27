# задача2
a = [3, 1, 3, 2, 1, 5]

b = len(set(a))
c = []
for num in a:
    if num not in c:
        c.append(num)
print(b)
print(c)

# задача3
text = "мама мыла раму мама"
words = text.split()
print(words)
d = {}
for word in words:
    d[word] = d.get(word, 0) + 1
print(d)

# задача4
word1 = "программа"
word2 = "грамматика"

set1 = set(word1)
set2 = set(word2)

print(sorted(set1 & set2))
print(sorted(set1 - set2))

# задача5


# задача6
# задача7
# задача8
# задача9
# задача10
