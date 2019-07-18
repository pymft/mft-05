def what(fn):
    def inner_fun(*args):
        out = fn(*args)
        return out
    return inner_fun


# fun = what(fun)
@what
def fun():
    return 10000000


print(fun())
