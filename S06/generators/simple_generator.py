def something():
    yield 10
    yield 20
    yield 3
    yield 15
    yield 1000
    yield 60
    yield 16



gen = something()

for i in gen:
    print(i)