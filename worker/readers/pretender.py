# -*- coding: UTF-8 -*-
# 伪装者，每次调用，都返回一个可用的代理IP地址

import user_agent  # 随机生成user_agent
import requests  # 加载解析地址库
from requests import RequestException  # 错误测试的返回值
from bs4 import BeautifulSoup as BS  # 加载解析HTML库
import os  # 处理文件

_path = os.path.dirname(os.getcwd())
# 获取ip
class proxy(object):
    # 构造请求头等
    def __init__(self):
        # 免费代理的网站列表
        # self.get_url_list = ['https://www.xicidaili.com/nn/','https://www.kuaidaili.com/free/']
        self.get_url = 'https://www.xicidaili.com/nn/'

        self.headers = {"User-Agent": user_agent.generate_user_agent()}  # 请求头内容,随机生成的
        self.test_url = 'https://httpbin.org/get'  # 测试网站地址
        self.file_path = "%s/res/list_ip.txt" %_path # 代理IP文件存放地址

        self.pages = 5  # 方案A：设定需要搜索页数
        self.from_page = 1  # 方案B：搜索起始页

    # 获取一个ip
    # 如果有文件，则从文件中获取一个IP，测试是否可用
    # 如果可用，则返回
    # 如果不可用，则删除这个IP，并测试下一个，直到有可用的，或者所有的都不可用，则创建副本
    # 如果没有文件，则解析网站，获取IP 保存文件，
    # 测试代理，并返回第一个可以使用的代理IP

    # 测试IP是否可用
    def _try_ip(self, i):
        try:  # 测试是否可用
            _response = requests.get(self.test_url, headers=self.headers, proxies={'http': i}, timeout=3)
            if _response.status_code == 200:
                print('验证成功，ip地址为：%s' % i)
                return _response
            else:
                self.remove(i)  # 删除ip
                print('返回值异常：%s' % _response.status_code)
                return
        except Exception as e:
            print('try失败：%s' % e)
            return

    # 解析代理网站页面，返回网页源码
    def _parse(self, url_path):
        try:
            _response = requests.get(url_path, headers=self.headers, timeout=3)
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

    # 从源码中提取ip信息
    @property
    def _get_list(self):
        if os.path.exists(self.file_path):  # 是否存在list版，存在则读取内容
            print('运气很好，找到对应的list文件，开始读取文件……')
            with open(self.file_path, 'r', encoding='utf-8') as _file:
                _list = eval(_file.read())

            print('读取成功：%s' % self.file_path)
            return _list
        else:  # 没有文件，则自己生产吧
            print('没有找到list文件，开始生成文件……')
            _list = []  # 创建返回列表

            # # 方案A：通过设定搜索页数来进行循环
            # for i_page in range(self.pages):
            #     data = self._parse(self.get_url + str(i_page))  # 获取网站源码
            #
            #     # 从源码中提取ip信息
            #     for i in data.find_all('tr'):
            #         _td = i.find_all('td')
            #         if _td:
            #             _ip = str(_td[1].text)
            #             _d = str(_td[2].text)
            #             _url = "%s:%s" % (_ip, _d)
            #             # 这里不用测试是否可用，因为不确定什么时间使用这个ip，可能使用时，也会失效
            #             _list.append(_url)

            # 方案B：通过增加页面深度来查询不同到页面，如果当前页面有可用的ip，不会查询下一页
            data = self._parse(self.get_url + str(self.from_page))  # 获取网站源码
            # 从源码中提取ip信息
            for i in data.find_all('tr'):
                _td = i.find_all('td')
                if _td:
                    _ip = str(_td[1].text)
                    _d = str(_td[2].text)
                    _url = "%s:%s" % (_ip, _d)
                    # 这里不用测试是否可用，因为不确定什么时间使用这个ip，可能使用时，也会失效
                    _list.append(_url)

            # 生成文件
            with open(self.file_path, 'a+') as _file:  # 新建一个文件
                _file.write(str(_list))

            print('生成文件成功：%s' % self.file_path)
            print('生成文件成功：%s' % self.file_path)
            return _list

    @property
    def get_one(self):  # 延用方案B的做法，方案A的做法，生成会花费很多时间
        _list = self._get_list  # 获取内容

        # 方案B，不停获取ip，直到得到内容
        if self._try_ip(_list[0]):  # 如果第一个可用，则返回
            print('返回IP')
            return _list[0]
        else:  # 删除ip，并重新获取
            self.remove()
            self.get_one()

        # #测试ip是否可用
        # for i_list in _list:
        #     if self._try_ip(i_list):
        #         print('提取一个代理IP：%s' % i_list)
        #         return i_list
        #     else:
        #         print('不可用IP：%s'%i_list)
        #         continue
        #
        # # 如果执行此部分，说明文件不存在，或者所有的ip全部不可用，则生产文件，并返回第一个代理IP
        # self._make_file()
        # return self.get_one()

    # 删除一个IP,如果没有IP 则删除文件
    def remove(self):
        with open(self.file_path, 'r').read() as file_r:
            list = eval(file_r)
            if len(list) == 1:
                os.remove(self.file_path)
            else:
                list = list[1:]  # 删除第一个
        with open(self.file_path, 'w') as file_w:
            file_w.write(list)


if __name__ == '__main__':
    a = proxy().get_one
    print(a)
