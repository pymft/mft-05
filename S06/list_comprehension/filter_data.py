def f(i):
    return i % 2 == 0

data = [1, 2, 3, 4, 5, 6, 7, 8,]
out = [i for i in data if i % 2 == 0]

filter(f, data)
print(out)