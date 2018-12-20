# coding=utf-8

# 加载豆瓣地址，并返回活动页面的地址


from test.douban import load  as url_load

import requests
from requests import RequestException

from bs4 import BeautifulSoup as bs

# 加载页面信息
_url = url_load()


# print(_url)
# 主函数
def main():
    # 解析页面
    _html = parsing_page(_url)

    # # 获取活动列表的地址列表
    # _list = list_page(_html)
    #
    # # 在活动列表中获取单个活动的地址列表
    # activity_list = list()
    # for i in _list:
    #     # 解析新地址
    #     _url['url'] = i
    #     _html = parsing_page(_url)
    #     _url_activity=url_activity(_html)
    #     #print(_url_activity)
    #     activity_list +=_url_activity
    #     # _url_activity =

    print(_html)


# 返回 活动列表页面 的 地址列表
def list_page(_html):
    # 获取列表页数
    _list_number = list_number(_html)

    # 生成列表
    page_list = list()
    i = 0
    while i < int(_list_number):
        if i == 0:
            e = _url['url']
            page_list.append(e)
        else:
            e = _url['url'] + '?start=' + str(i * 10)
            page_list.append(e)
        i += 1

    # 返回结果
    # print(page_list[2])
    return page_list


# 返回活动列表的页数
def list_number(html):
    # 获取信息主题
    df = html.find('div', class_='article')

    # 获取演出信息列表
    gd = df.find('div', class_='paginator')

    # 获取页码信息
    page_number_href = gd.find_all('a')

    g = list(reversed(page_number_href))

    # print(g[1].contents[0])
    return g[1].contents[0]


# 返回页面的源代码
def parsing_page(info):
    try:
        response = requests.get(info['url'], headers=info['headers'], proxies=info['proxies'], timeout=1)
        if response.status_code == 200:
            # 解析内容
            html = bs(response.text, 'html.parser')
            return html
        return None
    except RequestException:
        return None


# 返回单个活动列表中的活动地址列表
def url_activity(html):
    # 获取信息主题
    df = html.find('div', class_='article')

    # 获取演出信息列表
    gd = df.find('ul', class_='events-list')
    dge = gd.find_all("div", class_="title")

    # 生成列表
    _activity_list = list()

    # 将链接地址添加到列表中
    for i in dge:
        _i = i.find('a').get('href')
        _activity_list.append(_i)
        # print(_activity_list)

    # print(_activity_list)
    return _activity_list


def get_info(fd):
    print(fd.find('a').get('href'))


# 产检的单页解析，并保存
def jiexichanjian(info):
    _url['url'] = info['地址']
    _html = parsing_page(_url)

    j = {}

    gged = _html.find('div', class_='pre-d_checkdetail')

    info['正文'] = str(gged)

    print('多多岛：', gged)

    return info


# 解析食谱
def shipu(url):
    _url['url'] = url
    _html = parsing_page(_url)

    j = {}

    j1 = _html.find('div', class_='reimg_wrap').find('img').get('src')
    j['图片'] = j1

    j2 = _html.find('h2', class_='g-area-title').get_text()
    j['标题'] = j2

    j6 = _html.find_all('span', class_='list-item')
    j6_1 = []
    for i in j6:
        j6_1.append(i.get_text())
    j['作用'] = j6_1

    j3 = _html.find('p', class_='m-p').get_text()
    j['介绍'] = j3

    j4 = _html.find('h5', class_='g-arr-title').get_text()
    j5 = _html.find_all('li', class_='item')
    j5_1= []
    for i in j5:
        j5_1.append(i.get_text())

    print(j5_1)
    j['食材'] = j5_1

    j8 = _html.find('div', id='g-area').get_text()
    j['做法'] = j8

    # print('多多岛：', j)
    return j

if __name__ == '__main__':
    main()
