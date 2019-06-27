columns = 8
rows = 256//columns

for i in range(rows):
    for j in range(columns):
        # num = j * rows  + i
        num = i * columns + j
        print(num, chr(num), end='\t|\t')
    print()

