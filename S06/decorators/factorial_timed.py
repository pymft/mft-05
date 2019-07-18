import time


def decorator(fn):
    def inner(*args):
        t1 = time.time_ns()
        out = fn(*args)
        t2 = time.time_ns()
        print("Elapsed time = ", t2 - t1, "nanoseconds")
        return out

    return inner


@decorator
def factorial(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out


# factorial = decorator(factorial)


print(factorial(300))
