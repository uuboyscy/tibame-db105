import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for p in range(0,3):
    print(url)
    print('===============')
    res = requests.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div[class="title"] a')

    for n, t in enumerate(title):
        # print(t)
        title_name = t.text
        title_url = 'https://www.ptt.cc' + t['href']
        res_article = requests.get(title_url)
        soup_article = BeautifulSoup(res_article.text, 'html.parser')
        article_content = soup_article.select('div[id="main-content"]')
        all_article = article_content[0].text
        article_part = all_article.split('--')[0]
        f = open(r'./resource/test_%s_%s.txt'%(p, n), 'w', encoding='utf-8')
        f.write(article_part)
        f.close()
        print(title_name)
        print(title_url)
        print()

    last_page_url = soup.select('a[class="btn wide"]')
    new_url = 'https://www.ptt.cc' + last_page_url[1]['href']
    url = new_url
    # print('https://www.ptt.cc' + last_page_url[1]['href'])