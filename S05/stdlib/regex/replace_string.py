import re


text = """
12-07-1900
06-07-1990
"""
# "07/12/1900"

pat = r"(\d\d)-(\d\d)-(\d\d\d\d)"
rep = r"\2/\1/\3"


new_text = re.sub(pat, rep, text)
print(new_text)

# res = re.findall(pat, text)
# print(res)
# # match = res[0]
# # converted = [match[1], match[0], match[2]]
# # print('/'.join(converted))