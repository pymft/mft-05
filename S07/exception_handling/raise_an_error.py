class InvalidTypeOfFactorialError(TypeError):
    pass


class NegativeValueOfFactorialError(ValueError):
    pass


def fact(n):
    # if not type(n) == int:
    if not isinstance(n, int):
        raise InvalidTypeOfFactorialError("hey dude")
    if n < 0:
        raise NegativeValueOfFactorialError("negative int value is not valid bro!")
    out = 1
    while n > 0:
        out = out * n
        n = n - 1
    return out


# print(fact(-100))

try:
    print(fact(-100))
except InvalidTypeOfFactorialError as e:
    print("type e factorial is not valid", e.args   )
except NegativeValueOfFactorialError as e:
    print("negative value is not valid, dude!", e.args)
