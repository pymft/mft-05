def fact(n):
    # if not type(n) == int:
    if not isinstance(n, int):
        raise TypeError(str(type(n).__name__) + " is an invalid type")
    out = 1
    while n > 0:
        out = out * n
        n = n - 1
    return out


try:
    print(fact("hello"))
except TypeError as e:
    print(e.args)
