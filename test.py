import requests
from bs4 import BeautifulSoup
import re


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

base_url = 'http://www.qiushibaike.com/text/page/'  # 设定一个网址不变的部分，然后我们只要每次在这个后面加数字就可以了
# https://www.qiushibaike.com/text/page/
for num in range(1, 3): # 设置循环，让num分别等于1-10
    print('第{}页'.format(num))
    r = requests.get(base_url + str(num), headers = headers) #这里对网址进行一个修改

    #剩下的部分都是和原来的代码一样
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.find_all(class_=re.compile(r'article block untagged mb15 typs_'))
    print(len(divs))
    for div in divs:
        joke = div.span.get_text()
        print(joke)
        print('------')