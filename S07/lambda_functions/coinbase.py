import time
import urllib.request

link = "https://api.pro.coinbase.com/products/BTC-USD/candles/5m"


req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/66.0.2'})

req = urllib.request.urlopen(req)
html = req.read()
text = html.decode('utf-8')
data = eval(text)

res = max(data, key=lambda x: x[4] - x[3])
print(res)
print(res[-1])

print(time.ctime(res[0]))
