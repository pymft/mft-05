def fib_cpu(n):
    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b

    i = 2
    while i <= n:
        a, b = b, a+b
        i = i + 1
    return b


for i in range(10):
    print(fib_cpu(i))


def fib_memory(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    out = [0, 1]
    i =2
    while i <= n:
        out.append(out[-1] + out[-2])
        i += 1

    return out


for i in fib_memory(10):
    print(i)