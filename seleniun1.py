import requests
import urllib.request
import time
import random
from bs4 import BeautifulSoup
# webdriver用于调用浏览器
from selenium import webdriver
# By库用于指定HTML文件中DOM标签元素
from selenium.webdriver.common.by import By
# WebDriverWait库用于等待页面加载完毕
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions用于指定等待页面加载加载结束的条件
from selenium.webdriver.support import expected_conditions as EC

def get_url(url):
    time.sleep(1)
    return requests.get(url)

if __name__ == '__main__':
    browser = webdriver.Chrome()
    # 定义出发地
    dep_cities = ["西安", "厦门", "丽江", "杭州", "成都", "桂林", "青岛",
                  "大理", "上海", "昆明", "重庆", "广州", "南京",
                  "深圳", "武汉", "哈尔滨", "首尔", "香港", "普吉", "曼谷",
                  "澳门", "北京", "长春", "长沙",  "大理", "大连", "鄂尔多斯",
                  "恩施", "鄂州", "贵阳", "昆明", "开封", "海口", "台北",
                  "太原", "天津", "沈阳", "石家庄", "三门峡", "三明", "三沙",
                  "三亚", "商洛", "香港", "西宁", "厦门", "湘潭", "湘西",
                  "襄阳", "咸宁", "仙台", "仙桃", "咸阳", "孝感", "西昌市",
    ]
    for dep in dep_cities:
        # todo url 点击目的地选择js,headers arriveRecommend?dep 里
        strhtml = get_url("https://m.dujia.qunar.com/golfz/sight"
                          "/arriveRecommend?dep=" + urllib.request.quote(dep)
                          + "&exclude=&extensionImg=255,175")
        arrive_dict = strhtml.json()
        # print(arrive_dict)
        for arrive_item in arrive_dict["data"]:
            for arrive_item_1 in arrive_item["subModules"]:
                for query in arrive_item_1["items"]:
                    # 通过浏览器打开网页
                    browser.get("https://fh.dujia.qunar.com/?tf=package")

                    # EC.presence_of_all_elements_located()用于指定标志等待结束的DOM元素，
                    WebDriverWait(browser, 10).until(
                        # EC.presence_of_all_elements_located((By.ID, "depCity"))相当于id="depCity"
                        EC.presence_of_all_elements_located((By.ID, "depCity")))

                    # 清除输入框的内容
                    browser.find_element_by_xpath('//*[@id="depCity"]').clear()
                    # 将定义的出发地填入到出发地输入框
                    browser.find_element_by_xpath('//*[@id="depCity"]').send_keys(dep)
                    # 将目的地填入目的输入框
                    browser.find_element_by_xpath('//*[@id="arrCity"]').send_keys(query['query'])
                    # 单击“开始定制”按钮
                    browser.find_element_by_xpath("html/body/div[2]/div[1]/"
                                                  "div[2]/div[3]/div/div[2]/"
                                                 "div/a").click()
                    print("出发地点:{0},目的地:{1}".format(dep, query["query"]))

                    for i in range(100):
                        time.sleep(random.uniform(5, 6))
                        # 定位到搜索结果页码按钮，若定位不到表示结果为空，跳出循环
                        pagers = browser.find_elements_by_xpath('//*[@id="pager"]/div')
                        if pagers == []:
                            break

                        # 分块取出数据
                        # todo 使用 find_elements_by_class_name() 会报错（无效的选择器：不允许使用复合类名）
                        # 方法1:
                        routes = browser.find_elements_by_css_selector(".item.cf")
                        # 方法2:
                        # routes = browser.find_elements_by_css_selector("[class='item cf']")
                        # print(routes)

                        for route in routes:
                            result = {
                                "date": time.strftime('%Y-%m-%d', time.localtime(
                                    time.time())),
                                "dep": dep,
                                "arrive": query["query"],
                                "result": route.text
                            }
                            print(result)

                        # 指定页码和翻页
                        if i < 10:
                            pagers = browser.find_elements_by_xpath(
                                '//*[@id="pager"]/div/a[9]')
                            for a in pagers:
                                if a.text == "下一页":
                                    a.click()
                                    break

                    # 关闭浏览器

                    browser.close()

