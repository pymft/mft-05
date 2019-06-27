# n = 1000000
zeta = 0
pi_real = 3.14159265359
err = 0.0000001
i = 1

zeta_c = pi_real ** 2 / 6
err_c = err * pi_real / 3

while True:
    zeta = zeta + 1 / i ** 2     # T1

    if abs(zeta - zeta_c)/zeta_c < err_c:
        break
    i = i + 1


pi_approximate = (zeta * 6) ** 0.5

print(pi_real)
print(pi_approximate)
print(i)