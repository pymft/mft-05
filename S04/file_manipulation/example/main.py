fr = open('input.txt')
text = fr.read()
fr.close()

num, pat = text.split()
num = int(num)


fw = open('output.txt', mode='w')

for i in range(1, num+1):
    line = pat * i + '\n'
    fw.write(line)

fw.close()