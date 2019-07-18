def f(i):
    return i**2


rng = range(1_000_000)
out = [f(i) for i in rng]

out = map(f, rng)
