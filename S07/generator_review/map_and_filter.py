def f(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


def number_generator(n):
    i = 0
    while i < n:
        i += 1
        yield i




lst = number_generator(10)
# out_filter = [i for i in lst if is_even(i)]
out_filter = filter(is_even, lst)
print(list(lst))

print(list(out_filter))
# out_map = [f(i) for i in lst]
# out_map = map(f, lst)
# for i in out_map:
#     print(i)
