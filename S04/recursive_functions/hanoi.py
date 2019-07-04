def hanoi(n, start, middle, destination):
    if n == 1:
        print(start, "-->", destination)

    else:
        hanoi(n - 1, start, destination, middle)
        hanoi(1, start, middle, destination)
        hanoi(n - 1, middle, start, destination)


hanoi(4, "level 1", "level 2", "level 3")
