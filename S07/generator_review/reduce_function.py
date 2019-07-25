from functools import reduce


def f(a, b):
    return a + b


lst = [1, 2, 3, 4, 5, 6, 7]
res = reduce(f, lst)
print(res)

# 1 + (2 + (3 + (4 + (5 + (6 + 7)))))
#
# f(1, f(2, f(3, f(4, f(5, f(6, 7))))))
