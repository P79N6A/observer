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

    def todo(self):
        try:  # 如果被反扒，则解析json时会出错
            _response = requests.post(url=self.url, headers=self.headers, proxies=self.proxy_dict, data=self.data,
                                      verify=True)  # verify是否验证服务器的SSL证书)
            # print(_response.status_code,_response.text)

            _dict_data = json.loads(_response.text)  # 将字符串数据转换成字典数据，
            _get_post = _dict_data["pageData"]["resultData"]  # 将需要的爬取的字典数据存储在变量中
            # print('成功获取json:',_dict_data)
            print('成功获取json')

            print('完成提取数据的任务')
            return _get_post  # 返回数组
        except:
            # 这部分还没有完善
            print('被墙了')
            return None





if __name__ == '__main__':
    url = 'https://piao.damai.cn/164857.html'

    test = get_info(url)
    test.todo()
