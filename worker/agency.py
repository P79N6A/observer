# -*- coding: UTF-8 -*-
# 阅读者，专门找信息，专门爬取大麦网的演出活动地址，并保存为：get_url.csv


import requests  # 加载解析地址库
import json  # 解析json的库
import user_agent  # 随机生成user_agent
import re  # 用于提取剧名

from bs4 import BeautifulSoup as BS  # 加载解析HTML库


# 从大麦中获取列表信息
class get_post_damai:
    def __init__(self, URL, DATA, COOKIE, REFERER):
        self.url = URL  # 接受POST请求的地址
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "cookie": COOKIE,
            "referer": REFERER
        }
        self.data = DATA  # 请求内容
        self.proxy_dict = {
            # "http": "180.118.86.4:9000/",
            # "https": "180.118.86.4:9000/"
        }  # 这里需要制造代理







if __name__ == '__main__':
    url = 'https://piao.damai.cn/164857.html'

    test = get_info(url)
    test.todo()
