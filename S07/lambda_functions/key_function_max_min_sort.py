lst = [(1, 10), (2, 3), (4, 5), (6, 8), (-7, -8)]
mx = max(lst, key=lambda a: a[1] - a[0])
print(mx)