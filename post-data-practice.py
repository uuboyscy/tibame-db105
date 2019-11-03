import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

url = 'http://64b7860a.ngrok.io/homework_all/DB105'

post_data = {'pwd': 'REIxMDU=', '_hidden_info': '471829599'}
cookies = {'class_id': 'DB105', 'hidden_code': '1572765333'}
res = requests.post(url, data=post_data, cookies=cookies)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)