def distance(x, y, norm=2, whatever="whatever"):
    res = (x ** norm + y ** norm) ** (1 / norm)
    return res


print(distance(3, 4))
print(distance(3, 4, whatever="something"))
print(distance(3, 4, norm=1))
