def fact(n):
    print("salam, meghdare n = ", n,)
    if n == 0:
        print("OK, meghdare n = 0 bood, ")
        return 1
    res = n * fact(n - 1)
    print("khodafez, meghdare n = ", n, )
    return res


print(fact(5))