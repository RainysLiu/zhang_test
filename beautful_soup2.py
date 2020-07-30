import urllib.request
import urllib.parse
import re
import time
from bs4 import BeautifulSoup


# 获取智联招聘网页信息
class ZhiLianSpider(object):
    def __init__(self, jl, kw, start_page, end_page):
        # 保存到成员属性中，这样在其他的方法中就可以直接使用
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.items = []

    def handle_request(self, page):
        url = 'https://sou.zhaopin.com/?'
        data = {
            'jl': self.jl,
            'kw': self.kw,
            'p': page,
        }
        query_string = urllib.parse.urlencode(data)
        print(query_string)
        # 拼接url
        url += query_string
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                          '74.0.3729.169 Safari/537.36'
        }
        return urllib.request.Request(url=url, headers=headers)

    def parse_content(self, content):
        # 生成soup对象
        soup = BeautifulSoup(content, 'lxml')
        div_list = soup.find_all('div', class_="contentpile__content__wrapper " \
                                            "clearfix")
        # div_list = soup.find_all('div', class_="contentpile__content")
        # div_list = soup.find_all('div', class_="contentpile")
        print('div_list:{0}'.format(div_list))

        # 遍历所有的div，依次提取每一个工作的信息
        for div in div_list:
            zwmc = div.select( '.contentpile__content__wrapper__item__info__box'
                               '__jobname jobName')
            print(zwmc)
            # 公司名称
            # gsmc = div.select('.gsmc a')[0].text
            gsmc = div.select('.contentpile__content__wrapper__item__info__'
                              'box__cname__title company_title')
            print(gsmc)
            # 职位月薪

            # 工作地点

            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                # '职位月薪': zwyx,
                # '工作地点': gzdd,
            }
            self.items.append(item)

    def run(self):
        # 搞个循环
        for page in range(self.start_page, self.end_page + 1):
            print('正在爬取第%s页......' % page)
            # 拼接url的过程，构建请求对象
            request = self.handle_request(page)
            content = urllib.request.urlopen(request).read().decode('utf-8')
            # 给我请求对象，解析并且提取内容
            self.parse_content(content)
            print('结束爬取第%s页' % page)
            time.sleep(2)

        # 将所有的工作保存到文件中
        string = str(self.items)
        with open('work.txt', 'w', encoding='utf-8') as fp:
            fp.write(string)

def main():
    # 输入工作地点
    jl = input('请输入工作地点:')
    # 输入工作关键字
    kw = input('请输入关键字:')
    # 输入起始页码
    start_page = int(input('请输入起始页码:'))
    # 输入结束页码
    end_page = int(input('请输入结束页码:'))
    zhilian = ZhiLianSpider(jl, kw, start_page, end_page)
    zhilian.run()

if __name__ == '__main__':
    main()