import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/M.1572705581.A.928.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

article_content = soup.select('div[id="main-content"]')
all_article = article_content[0].text
article_part = all_article.split('--')[0]
print(article_part)

f = open(r'./test.txt', 'w', encoding='utf-8')
f.write(article_part)
f.close()
