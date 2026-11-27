import sys

a = [i for i in range(-500, 500) if sys.getrefcount(i) > 2]
print(a)
