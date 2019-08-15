# f = open("output.txt", mode="w")
# f.write("hello")
# f.close()

with open("output.txt", mode="w") as f:
    f.write("hello")

