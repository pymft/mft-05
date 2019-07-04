def factorial(n):
    out = 1
    for i in range(n + 1):
        out = out * i
    return out



factorial(10)






n = 5
k = 3
n_fact = factorial(n)
k_fact = factorial(k)
n_k_fact = factorial(n-k)



combination = n_fact / (k_fact * n_k_fact)
print(combination)