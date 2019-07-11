import re

text = """
user@DOMAIN.com
asghar@yahoo.com
my_email@gmail.com
"""

pattern = r"(\w+)@(\w+)\.(\w+)"
# pattern = "(\\w+)@(\\w+)\\.(\\w+)"

result = re.findall(pattern, text)
print(result)
