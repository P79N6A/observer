# -*- coding: UTF-8 -*-

# 公共库
from urllib.parse import urlparse  # 拆分URL
import user_agent  # 随机生成user_agent
import time
import os  # 转换内容 ，并提取数据

from worker.readers.pretender import proxy  # 获取代理IP
# 加载解析地址库
import requests
from requests import RequestException

# 加载解析HTML库
from bs4 import BeautifulSoup as BS


# 加载保存库
# from other.serving import todo





# 爬取活动列表页面的地址列表，返回列表，包含所有活动列表页面的URL地址
def get_list(_html):
    # 获取列表页数
    _page_number = get_number(_html)

    # 生成所有活动列表的地址
    url_list = list()

    # 组装列表
    for i in range(_page_number):
        if i == 0:
            e = url
            url_list.append(e)
        else:
            e = url + '?start=' + str(i * 10)
            url_list.append(e)

    # 测试返回活动页数
    # print('活动页数：',len(url_list))
    return url_list


# 返回活动列表的页数
def get_number(_html):
    # 获取信息主题
    df = _html.find('div', class_='article')

    # 获取演出信息列表
    gd = df.find('div', class_='paginator')

    # 获取页码信息
    try:
        page_number_href = gd.find_all('a')
        g = list(reversed(page_number_href))
    except AttributeError:
        print("提示：获取活动列表的页数时失败，这个活动列表只有1页")
        return 1

    # 返回结果
    # print(int(g[1].contents[0]))
    return int(g[1].contents[0])


# 获取所有活动列表中的活动的地址
def get_url(_list):
    _get_url = list()

    for i in _list:
        # print(i)
        # 组成新url
        _html = get_parse(URL_Info(i).douban())

        # 获得活动地址
        _activity = get_activity(_html)

        # 保存到列表中
        _get_url += _activity

    # 返回列表
    # print(_get_url)
    return _get_url


# 返回单个活动列表中的活动地址列表
def get_activity(_html):
    # 获取信息主题
    df = _html.find('div', class_='article')

    # 获取演出信息列表
    gd = df.find('ul', class_='events-list')
    dge = gd.find_all("div", class_="title")

    # 生成列表
    _activity_list = list()

    # 将链接地址添加到列表中
    for i in dge:
        _activity_list.append(i.find('a').get('href'))
        # print(_activity_list)

    # print(_activity_list)
    return _activity_list


# 清洗地址数据
def clean_url(_list):
    # 保存数据到本地文件

    # 对比地址和列表中到地址
    _clean = list()

    _clean = _list

    # 返回结果，目前还没做
    # print(_clean)
    return _clean


# 获取每条活动的信息
def get_info(case_url):
    # 装载url
    _url_info = URL_Info(case_url).douban()

    # 解析页面
    _html = get_parse(_url_info)

    # 建立字典
    _info = {'封面': _html.find('img', id='poster_img').get('src'), '标题': _html.find('h1', itemprop='summary').get_text(),
             '时间': _html.find('div', class_='event-detail').find('li').get_text(),
             '城市': _html.find('span', itemprop='region').get_text(),
             '地点': _html.find('span', itemprop='street-address').get_text(),
             '票价': _html.find('span', itemprop='ticketAggregate').get_text(),
             '类型': _html.find('a', itemprop='eventType').get_text(), '内容': _html.find('div', id='edesc_s').get_text()}

    # 获取活动的封面地址

    # 获取活动的标题

    # 获取活动的时间

    # 获取活动的城市

    # 获取活动的地点

    # 获取活动的票价

    # 获取活动的类型

    # 获取活动的内容

    # print("显示单个活动的内容：",_info)
    return _info


if __name__ == '__main__':
    _i = get_news('杏仁豆腐心').main()
