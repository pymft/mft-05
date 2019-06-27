
str.maketrans()
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq
rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu
ynnjw ml rfc spj."""

# text = "AZab xyz ()"
out = ""

# mapping = {' ': ' ', 'a': 'c', 'b': 'd',     'y': 'a', 'z': 'b'}


for c in text:
    if 65 <= ord(c) <= 91:
        converted = chr(65 + ((ord(c) + 2 - 65) % 26))
    elif 97 <= ord(c) <= 122:
        # tmp = 0
        # if c in ['y', 'z', 'Y', 'Z']:
        #     tmp = 26
        #
        # converted = chr(ord(c) + 2 - 0)

        # converted = mapping[c]
        converted = chr (97 + ((ord(c) + 2 - 97) % 26))
    else:
        converted = c
    out = out + converted

print(out)