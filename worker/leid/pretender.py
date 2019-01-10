# -*- coding: UTF-8 -*-
# 伪装者，每次调用，都返回一个可用的代理IP地址

import user_agent  # 随机生成user_agent
import requests  # 加载解析地址库
from requests import RequestException  # 错误测试的返回值
from bs4 import BeautifulSoup as BS  # 加载解析HTML库
import os  # 处理文件


# 获取ip
class proxy(object):
    # 构造请求头等
    def __init__(self):
        # 免费代理的网站列表
        # self.get_url = 'https://www.kuaidaili.com/free/'
        self.get_url = 'https://www.xicidaili.com/nn/'

        # 请求头内容
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "Cookie": "",
            "Referer": ""
        }

        # 测试网站地址
        self.test_url = 'https://httpbin.org/get'

        # 代理IP文件存放地址
        self.file_path = "res/ip.txt"

    # 测试代理，并返回第一个可以使用的代理IP
    @property
    def get_one(self):
        # 判断是否有代理列表文件
        if os.path.exists(self.file_path):  # 如果有文件则读取文件内容
            with open(self.file_path, 'r') as _file:
                for i in _file.readlines():
                    if self._try_ip(i):
                        print('提取一个代理IP', i)
                        return i
                    else:
                        continue

        # 如果执行此部分，说明文件不存在，则生产文件，并返回第一个代理IP
        with open(self.file_path, 'w') as _file:
            for i in self._get_list:  # 遍历获取到列表
                try:
                    response = requests.get(self.test_url, headers=self.headers, proxies={'http': i}, timeout=3)
                    if response.status_code == 200:
                        _file.write(i + '\n')
                        print('可用IP：%s' % i)
                    else:
                        print('无效IP：%s' % response.status_code)
                except Exception as e:
                    print('验证失败：%s' % e)

    # 测试IP是否可用
    def _try_ip(self,i):
        try:  # 测试是否可用
            _response = requests.get(self.test_url, headers=self.headers, proxies={'http': i}, timeout=3)
            if _response.status_code == 200:
                print('验证成功，ip地址为：%s' % i)
                return _response
            else:
                print('返回值异常：%s' % _response.status_code)
                return None
        except Exception as e:
            print('try失败：%s' % e)
            return None

    # 获得代理地址
    @property
    def _get_list(self):
        data = self._parse  # 获取列表

        _list = []  # 创建返回列表

        # 提取信息
        for i in data.find_all('tr'):
            _td = i.find_all('td')
            if _td:
                _ip = str(_td[1].text)
                _d = str(_td[2].text)
                _url = "%s:%s" % (_ip, _d)
                _list.append(_url)

        print('获取列表成功')
        return _list

    # 解析代理网站页面
    @property
    def _parse(self):
        try:
            _response = requests.get(self.get_url, headers=self.headers, timeout=3)
            if _response.status_code == 200:
                # 自行转码
                _response.encoding = 'UTF-8'
                # 解析内容
                page_source = BS(_response.text, 'html.parser')

                # print(response.text)
                print('获取页面资源成功')
                return page_source
            else:
                print('解析代理网站时出现错误', _response.status_code)
                return None
        except RequestException:
            print('解析代理网站时出现错误', RequestException)
            return None


if __name__ == '__main__':
    a=proxy().get_one
    print(a)
