import requests
import urllib.request
import time
from multiprocessing import Pool

# 爬取touch.qunar.com(去哪儿网)电商平台数据


def get_list(dep, item):
    url = "https://touch.dujia.qunar.com/list?modules=list,bookingInfo," \
          "activityDetail&dep={0}&query={1}&dappDealTrace=true&" \
          "mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%&" \
          "cfrom=zyx&it=dujia_hy_destination&page=home&date=&needNoResult" \
          "=true&originalquery={2}&limit=0,24&includeAD=true&qsact=" \
          "search".format(urllib.request.quote(dep), urllib.request.quote(item),
                          urllib.request.quote(item))
    time.sleep(1)
    response = requests.get(url)
    routeCount = int(response.json()["data"]["limit"]["routeCount"])

    for limit in range(0, routeCount, 24):
        # ………………url 访问不了（待解决）
        url = "	https://touch.dujia.qunar.com/list?modules=list" \
              "%2CbookingInfo%2CactivityDetail&dep={0}&query={1}" \
              "&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%" \
              "E8%87%AA%E7%94%B1E8%A1%8C&cfrom=zyx&it=" \
              "dujia_hy_destinaton&date=&needNoResult=true&" \
              "originalquery={2}&limit={3},24&includeAD=true&" \
              "qsact=search".format(urllib.request.quote(dep),
                                    urllib.request.quote(item),
                                    urllib.request.quote(item), limit)
        time.sleep(1)
        response = requests.get(url)
        result = {
            "date": time.strftime('%Y-%m-%d', time.localtime(time.time())),
            "dep": dep,
            "arrive": item,
            "limit": limit,
            "result": response.json()
        }
        print(result)

def get_json(url):
    response = requests.get(url)
    time.sleep(1)
    return response.json()


if __name__ == '__main__':
    # 1、获取出发地点信息(自由行)
    url = "https://touch.dujia.qunar.com/depCities.qunar"
    dep_dict = get_json(url)
    for dep_item in dep_dict["data"]:
        # print(dep_item, end="\n")
        # 获取地名
        for dep in dep_dict["data"][dep_item]:
            # 所有地名组成的列表
            a = []
            # 2、根据出发地站点获取目的地#
            # url来源于JS下arriveRecommend？dep
            url = "https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?" \
                  "dep={0}&exclude=&extensionImg=255,175".format(
                urllib.request.quote(dep))
            time.sleep(1)
            arrive_dict = get_json(url)
            # print(arrive_dict)
            for arrive_item in arrive_dict["data"]:
                for arrive_item_1 in arrive_item["subModules"]:
                    # print(arrive_item_1)
                    for query in arrive_item_1["items"]:
                        # print(query)
                        # print(query["query"])
                        if query["query"] not in a:
                            a.append(query["query"])
            # print(a)

            # 3、获取产品列表(XHR下list?modules)
            for item in a:
                get_list(dep, item)

