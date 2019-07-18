import time

def decorator(fn):
    def inner(*args):
        t1 = time.time_ns()
        out = fn(*args)
        t2 = time.time_ns()
        print("Elapsed time = ", t2 - t1, "nanoseconds")
        return out

    return inner

#
# def len_new(o):
#     out = len(o)
#     return out
#
#
# def max_new(*args):
#     out = max(*args)
#     return out
#
#
# def range_new(*args):
#     out = range(*args)
#     return out
#


len_new = decorator(len)
print(len_new([1, 2, 3]))

sum_new = decorator(sum)
print(sum_new(range(10000000)))

range_new = decorator(range)
print(range_new(2, 100, 50))
