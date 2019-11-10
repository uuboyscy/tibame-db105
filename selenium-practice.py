from selenium.webdriver import Chrome
import requests

driver = Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)
driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookies = driver.get_cookies()

print(cookies)

driver.close()

ss = requests.session()

for c in cookies:
    ss.cookies.set(c['name'], c['value'])

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

res = ss.get(url)
print(res.text)
