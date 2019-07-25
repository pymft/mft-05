def f_map(n):
    return n ** 2


def is_even(n):
    return n % 2 == 0


lst = [1, 2, 3, 4, 5, 6, 7, 8]
out = (f_map(i) for i in lst if is_even(i))

print(out)

# out = map(f_map, filter(is_even, lst))
# print(list(out))
