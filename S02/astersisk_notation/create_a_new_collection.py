a = (1, 2, 3)
b = (10, 20)

c = (0, *a, 10000, *b, 1000000)
d = a + b    # or:  d = (*a, *b)
print(c)

dct_a = {'name': 'John'}
dct_b = {'last name': 'Lock'}

dct_new = {**dct_a, **dct_b}
print(dct_new)