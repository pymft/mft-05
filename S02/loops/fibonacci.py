n = 10

a, b = 0, 1

i = 0
print(a)

i = i + 1
print(b)


while i < n:
    i += 1
    a, b = b, a+b
    print(b)

