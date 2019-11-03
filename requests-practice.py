import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)