import string

rot = 16

lower = string.ascii_lowercase   # "abcdefghijklmnopqrstuvwxyz"
lower_map = lower[rot:] + lower[:rot]

upper = string.ascii_uppercase
upper_map = upper[rot:] + upper[:rot]

inputs = upper + lower
outputs = upper_map + lower_map

text = "rovvy"

mapping_dictionary = str.maketrans(inputs, outputs)
result = text.translate(mapping_dictionary)
print(result)