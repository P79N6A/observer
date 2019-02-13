# -*- coding: UTF-8 -*-
# 阅读者，通过从阅读者那里获取内容，并对内容进行解析，同时生成爬虫报告
# 公共库
from urllib.parse import urlparse  # 拆分URL
import user_agent  # 随机生成user_agent
import time
import os  # 转换内容 ，并提取数据
import requests  # 加载解析地址库
from bs4 import BeautifulSoup as BS  # 加载解析HTML库
from requests import RequestException  # try库

# 内部库
from worker.readers.pretender import proxy  # 获取代理IP
# 解析豆瓣-同城活动
class douban_activity:
    def __init__(self):
        pass