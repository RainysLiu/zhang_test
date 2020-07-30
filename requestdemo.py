import urllib.request as ur
import requests,json

# 爬取有道翻译网
def translant(word):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    form_data = {
    'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict',
    'client': 'fanyideskweb', 'salt': '15600909590996',
    'sign': 'f2d05f89c27c383c84d46cd579d5daf9', 'ts': '1560090959099',
    'bv': 'c4e95e621267f4d4577f554f2869b772', 'doctype': 'json',
    'version': '2.1', 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME',
    'typoResult':'False'
    }
    response = requests.post(url, data=form_data)
    # print(response)
    content = json.loads(response.text)
    # content = json.load(response)
    # print(content)
    result = content['translateResult'][0][0]['tgt']
    print("翻译结果为：{0}".format(result))

if __name__ == '__main__':
    Word = input("请输入需要翻译的文字：")
    translant(word=Word)