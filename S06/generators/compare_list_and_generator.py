def nums(n):
    i = 1
    while i <= n:
        yield i
        i += 1


upper = 20_000_000
# numbers = list(nums(upper))
numbers = nums(upper)
out = 0
for i in numbers:
    out += i

print(out)