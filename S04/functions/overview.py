n = 5
k = 3

n_fact = 1
for i in range(n + 1):
    n_fact = n_fact * i


k_fact = 1
for i in range(k + 1):
    k_fact = k_fact * i


n_k_fact = 1
for i in range((n-k) + 1):
    n_k_fact = n_k_fact * i



combination = n_fact / (k_fact * n_k_fact)
print(combination)