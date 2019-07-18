def fun(inp):
    out = []
    for i in range(len(inp)):
        temp = 1
        for j in range(len(inp)):
            if not j == i:
                temp = temp * inp[j]

        out.append(temp)
    return out


def new_fun(lst):
    out = []

    zeros = lst.count(0)
    if zeros > 1:
        return [0 for v in lst]
    elif zeros == 1:
        pass
    else:
        A = 100
        return [A/v for v in lst]



lst = [1, 2, 3, 9]

out = fun(lst)   #  [30, 10, 6, 15]
print(out)