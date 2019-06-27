import time

n = 2000000
zeta = 0
pi_real = 3.14159265359
err = 0.000001

t_start = time.time()

for i in range(1, n + 1):
    zeta = zeta + 1 / i ** 2

t_stop = time.time()
print("Elapsed time = ", t_stop - t_start)

pi_approximate = (zeta * 6) ** 0.5

print(pi_real)
print(pi_approximate)
err = abs(pi_real - pi_approximate) / pi_real
print(err)
