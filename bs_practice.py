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
#print(soup)

logo = soup.findAll('a', {'id': 'logo'})
print(logo[0].string)
print(logo[0].text)

title = soup.findAll('div', {'class': 'title'})
print(title[0])

title_str = title[0].findAll('a')
print(title_str[0].text)
print('https://www.ptt.cc' + title_str[0]['href'])
print()

for t in title:
    each_titles = t.findAll('a')
    each_title = each_titles[0]
    print(each_title.text)
    print('https://www.ptt.cc' + each_title['href'])
    print()
