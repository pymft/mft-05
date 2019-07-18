
def is_right(a, b, c):
    lst = [a, b, c]
    lst.sort()
    a, b, c = lst
    if c ** 2 == a ** 2 + b ** 2:
        return True

    return False




