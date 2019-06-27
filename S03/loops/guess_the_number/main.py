import math
from random import randint

upper = 8

secret = randint(1, upper)
print(secret)

limit = int(math.log2(upper))
win = 0

for i in range(limit):
    guess = int(input(">"))

    if guess > secret:
        print("guess number greater than secret")
    elif guess < secret:
        print("guess number less than secret")
    else:
        win = 1
        break

if win == 1:
    print("Bingo")
else:
    print("Haaaa HAaaa")

