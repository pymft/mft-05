def fun(inp):
    # inp.pop()

    samte_raste_mosavi = inp + 1
    print("inp id", id(inp))
    inp = samte_raste_mosavi
    print("inp id", id(inp))
    return inp


num = 100000
print(id(num))
num = int(fun(num))
print(id(num))
