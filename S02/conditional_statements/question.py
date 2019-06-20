

#       10            20            30          40
# ------###############-------------#############->

num = 25
# cond = (10 <= num <= 20) or (30 <= num <= 40)
cond = (10 <= num < 40) and not (20 < num < 30)


if (10 <= num < 40) and not (20 < num < 30):
    print("the number is in the range")
else:
    print("is not the range")
