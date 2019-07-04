def fib(n):
    if n in (0, 1):
        return n

    return fib(n-1) + fib(n-2)


def fib_sequence(n):
    out = []
    for i in range(n):
        out.append(fib(i))

    return out


# print(fib_sequence(30))
print(fib(3))