# http://mft-python.ir/its/src/decorators/simple.logger/

import time

def logger(fn):

    def inner(*args):
        res = fn(*args)

        log_str = f'"{time.time()}","{fn.__name__}","{args}","{res}"\n'
        f = open('logs.csv', mode='a')
        f.write(log_str)
        f.close()

        return res
    return inner


@logger
def my_sum(a, b):
    return a+b

my_sum = logger(my_sum)

@logger
def my_mul(a, b):
    return a*b


print(my_mul(1, 2))
print(my_sum(2, 3))
print(my_mul(1232, 2234))
print(my_sum(2342, 332))
