# 这里实现了解析地址，并获取了网站到内容
import ssl
import config as _config
import requests

from bs4 import BeautifulSoup

# 设置爬虫地址，以后变成配置文件
url = _config.url

# 设置请求头
headers = _config.headers

# 设置代理
proxies = _config.proxies


# 打开url
def open_url_get(url,headers,proxies):
    # 添加ssl证书
    ssl._create_default_https_context = ssl._create_unverified_context

    # 设置Request，格式设置
    request = requests.get(url, headers=headers, proxies=proxies, timeout=1)

    # 打开地址，并赋值到response


    # ？
    the_page = request.text

    return the_page


'''def open_url_post(url):
    # 添加ssl证书
    ssl._create_default_https_context = ssl._create_unverified_context

    # 设置data
    data = {
        'name': 'Germey'
    }

    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Host': 'httpbin.org'
    }

    # 设置Request，格式设置
    request = urllib.request.Request(url=url, data=data, headers=headers, method='GET')

    # 打开地址，并赋值到response
    response = urllib.request.urlopen(request)

    # ？
    the_page = 11

    return the_page
'''

_the_page = open_url_get(url,headers,proxies)

#print(_the_page)

a = BeautifulSoup(_the_page,'xml')
# 已经可以读出内容了
print(a.body.string)

""""# 查找内容
a = r'<noscript><iframe src="//[^~]" height="0" width="0" style="display:none;visibility:hidden">'
rand= re.search('<title>',_the_page)
print(rand.group())"""



#print(re.findall(a, _the_page))
