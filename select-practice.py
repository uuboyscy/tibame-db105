from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

tmp_html = res.read().decode('utf-8')

soup = BeautifulSoup(tmp_html, 'html.parser')

logo = soup.select('a[id="logo"]')
print(logo)

title = soup.select('div[class="title"]')
print(title[0].a.text)



