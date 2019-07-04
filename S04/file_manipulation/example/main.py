def extract_data(text):
    num, pat = text.split()
    num = int(num)
    return num, pat


def generate_pat(num, pat):
    out = ''
    for i in range(1, num + 1):
        # line = pat * i
        # line = pat * (2*i-1)
        line = pat + " " * (2*i-3) + pat
        line = line.center(2*num - 1)

        out += line + '\n'

    return out


fr = open('input.txt')
num, pat = extract_data(fr.read())
fr.close()

fw = open('output.txt', mode='w')
fw.write(generate_pat(num, pat))
fw.close()