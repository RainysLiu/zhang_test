import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.find_all("a", href=re.compile("^(/.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks


# 获取所有外链的列表
def getExternallLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that do not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def test_return_value(fun):
    def test(*args,**kwargs):
        result = fun(*args,**kwargs)
        if result is None:
            print("无返回值")
        else:
            print("返回值为%s" %result)
            # return result
    return test

# url拆分
@test_return_value
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

# Collects a list of all external URLs found on the site
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    print(internalLinks)
    externalLinks = getExternallLinks(bsObj, splitAddress(siteUrl)[0])
    print(externalLinks)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks("http:" + link)





# def test():
#     def


if __name__ == '__main__':

    # getAllExternalLinks("http://oreilly.com")
    # html = urlopen("http://oreilly.com")
    # bsObj = BeautifulSoup(html, 'lxml')
    # address = 'http://oreilly.com'
    # addressParts = address.replace("http://", "").split("/")
    # print(addressParts)
    # internalLinks = getInternalLinks(bsObj, addressParts[0])
    # print(internalLinks)


    # def fun(a, b, c=3, d=4):
    #     pass
    #
    # fun()


    # print(test_return_value(lambda :10))
    # print(test_return_value)

    # res = test_return_value(splitAddress)('http://baidu.com')
    res = splitAddress('http://baidu.com')
    print(res)






