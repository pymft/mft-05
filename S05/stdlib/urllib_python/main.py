import re
import urllib.request

url = "https://me.ucmerced.edu/faculty"
fp = urllib.request.urlopen(url)
html = fp.read()

text = html.decode("utf8")

email = re.findall(r'mailto:[a-zA-Z\.-]+@[\w\.-]+',text)
print(email)
