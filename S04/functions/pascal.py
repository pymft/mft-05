def factorial(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i
    return out


def combination(n, k):
    value = factorial(n) / (factorial(k) * factorial(n - k))
    return int(value)


def pascal_row(m):
    out = []

    for i in range(m + 1):
        tmp = combination(m, i)
        out.append(tmp)

    return out


def pascal(rows):
    last_line = pascal_row(rows)
    width = len(str(last_line))
    for i in range(rows):
        row = pascal_row(i)
        line = str(row).center(width)
        print(line)


pascal(10)
