n = 10

a, b = 0, 1
print(a)
print(b)

for _ in range(n-2):
    a, b = b, a+b
    print(b)
