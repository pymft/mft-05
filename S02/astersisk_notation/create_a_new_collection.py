a = (1, 2, 3)
b = (10, 20)

c = (0, *a, 10000, *b, 1000000)
d = a + b    # or:  d = (*a, *b)
print(c)