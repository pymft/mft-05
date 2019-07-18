import time


def call_it(fn):
    def inner():
        return fn()
    return inner()


@call_it
def now():
    return time.ctime()

