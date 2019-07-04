def multiply(m, n):
    return m + n


def sum_of_number(n):
    res = 0
    for i in range(1, n + 1):
        res += i

    return res


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(0))
