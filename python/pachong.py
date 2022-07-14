from email import header
import requests
url = 'http://www.dianping.com'
header = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.3'}
res = requests.get(url, headers=header)
#res.encoding = 'utf-8'
print(res.encoding)
print(res.text)
print(res.status_code)
