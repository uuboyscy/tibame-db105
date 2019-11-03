from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent': user_agent}

#url = 'http://64b7860a.ngrok.io/hello_get?name=Allen&age=22'
url = 'https://www.ptt.cc/bbs/movie/index.html'
#url = 'http://64b7860a.ngrok.io/get_headers'

req = request.Request(url = url, headers = headers)

#res = request.urlopen(req)
res = request.urlopen(url)

tmp_html = res.read().decode('utf-8')

print(tmp_html)