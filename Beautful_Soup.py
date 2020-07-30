import requests
from bs4 import BeautifulSoup

# 爬取中国旅游网
url = 'http://www.cntour.cn/'
respnse = requests.get(url)
soup = BeautifulSoup(respnse.text, 'lxml')
# print(soup)
data = soup.select('#main > div > div.mtop.firstMod.clearfix > ' 'div.centerBox > ul.newsList > li > a')
print(data)
for item in data:
    result = {'title': item.get_text(),
              'link': item.get('href')
            }
    print(result)