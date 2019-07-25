def fun(fn, args):
    return fn(*args)


res = fun(lambda x, y: x + y, (1, 10))
print(res)
