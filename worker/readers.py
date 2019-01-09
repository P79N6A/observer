# -*- coding: UTF-8 -*-
# 通过从阅读者那里获取内容，并对内容进行解析，同时生成爬虫报告

# 加载header信息
import re
import time
from lxml import etree
import pandas as pd

from worker.url_info import URL_Info

# 加载解析地址库
import requests
from requests import RequestException

import user_agent  # 随机生成user_agent
import json
import csv

import pymongo

from bs4 import BeautifulSoup as BS  # 加载解析HTML库

# 导入获取地址的库
# from worker.writers import save_list as Save
from worker.agency import get_post_damai


# 获取大麦的演出列表
class get_show_list(object):
    # 构造请求头等
    def __init__(self):
        # 大麦网接受POST请求的地址
        self.post_url = 'https://search.damai.cn/searchajax.html'

        # 以后要试图用别到方法获取
        self.Cookie = 'isg=BKys-EXc3E7Cn82CThRo44Q6f4zeZVAPNQZk9QbtuNf6EUwbLnUgn6KiNVmpgohn; l=aB8neGmpyhCp3pDBtManBsRP-xrxygBP2j0yxMazZiYGdP8ZuXKbBjno-Vw6d_qC55oy_X-iI; x5sec=7b226d65632d67756964652d7765623b32223a226330353961323833626333396639623439346663663365343461633235313234434d4341782b4546454a617937346a353176585946673d3d227d; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201546617582%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201546617582%7D%7D; x_hm_tuid=PGrpHppNc7p6qeO6rXzlt1Xkss1FsDkItpzuBytBQ5KWbMnMwqH0Nz0UiMR82FQq; _uab_collina=154633349240746853818272; destCity=%u6B66%u6C49; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371'

        # 请求内容
        self.data = {
            "cty": "武汉",
            "ctl": "话剧歌剧",
            "tsg": "0",
            "order": "0"
        }
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


        # 上级页面
        self.Referer = 'https://search.damai.cn/search.htm'

        # 步骤参数
        self.steps = 0

        # 设置返回值
        self._value = []

    # 主函数
    def _main(self):
        # 解析演出列表页面，返回包含演出基本信息的数组
        _get_post = get_post_damai(URL=self.post_url, DATA=self.data, COOKIE=self.Cookie, REFERER=self.Referer).get_value
        print('获取页面信息成功')

        # 获取有用信息
        for j in range(len(_get_post)):
            # 为了让代码更简洁，做了一个赋值
            _info = _get_post[j]

            # 获取有用的信息,属性
            _j = dict(标题=_info['name'], 副标题=_info['subhead'], 地点城市=_info['venuecity'], 演出场所=_info['venue'],
                      演出时间=_info['showtime'], 演出状态=_info['showstatus'], 演出类型=_info['subcategoryname'],
                      projectid=_info['projectid'], imgurl=_info['imgurl'], 最低票价=_info['price'],
                      最高票价=_info['pricehigh'], 信息属性=self.steps)

            # 添加剧名
            if bool(re.search('《[^》]+》', _info['name'], flags=0)):  # 如果搜得到《》，则赋值到'剧名'
                _j['剧名'] = re.search('《[^》]+》', _info['name'], flags=0).group()
            else:  # 如果提取不到《》，则写入日志
                # 之后在分析是，如果是空值，则不处理
                _j['剧名'] = None
                with open("Running_log.txt", 'a+', encoding='utf-8') as _log:
                    text = '\n获取剧名失败，需要特殊处理：' + str(_info['name'])
                    _log.write(text)

            self._value.append(_j)

    @property
    def get_value(self):
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
    @property
    def get_value(self):
        self._main()

        return self._value


# 在大麦中到演出详情中，补全所有信息属性为0的活动的信息
class get_info():
    def __init__(self):
        # 数据库
        self.data_table = pymongo.MongoClient('mongodb://localhost:27017/')["swarm"]['show_list']

        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "cookie": 'isg=BKys-EXc3E7Cn82CThRo44Q6f4zeZVAPNQZk9QbtuNf6EUwbLnUgn6KiNVmpgohn; l=aB8neGmpyhCp3pDBtManBsRP-xrxygBP2j0yxMazZiYGdP8ZuXKbBjno-Vw6d_qC55oy_X-iI; x5sec=7b226d65632d67756964652d7765623b32223a226330353961323833626333396639623439346663663365343461633235313234434d4341782b4546454a617937346a353176585946673d3d227d; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201546617582%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201546617582%7D%7D; x_hm_tuid=PGrpHppNc7p6qeO6rXzlt1Xkss1FsDkItpzuBytBQ5KWbMnMwqH0Nz0UiMR82FQq; _uab_collina=154633349240746853818272; destCity=%u6B66%u6C49; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371',
            "referer": 'https://search.damai.cn/search.htm'
        }

        # 代理
        self.proxy_dict = {
            # "http": "180.118.86.4:9000/",
            # "https": "180.118.86.4:9000/"
        }
        # 默认地址头
        self._url_header = 'https://piao.damai.cn/'

        # 步骤参数
        self.steps = 1

    # 获取满足属性条件都所有信息的列表
    def updata(self):
        # 获取内容
        _list = self.data_table.find({'信息属性': 0})

        # 逐个查询
        for i in _list:
            # 拼接查询地址
            _url = self._url_header + str(i['projectid']) + '.html'
            # print(_url)

            # 获取源代码
            _get_info = self._get_info(_url)

            # 获取有用信息list
            updata_data = self._extract(_get_info)
            # print('返回内容：',updata_data)

            # 更新内容
            self.data_table.update({'projectid': i['projectid']}, {'$set': updata_data})
            print('完成更新 %s' % i['标题'])
            time.sleep(10)  # 设置5秒定时，避免反爬

    # 获取页面内容
    def _get_info(self, Url):
        try:
            # 获取get数据包,verify是否验证服务器的SSL证书
            response = requests.get(url=Url, headers=self.headers, proxies=self.proxy_dict, verify=True, timeout=1)

            if response.status_code == 200:
                # 自行转码
                response.encoding = 'UTF-8'
                # 解析内容
                page_source = BS(response.text, "lxml")

                # print(response.text)
                return page_source
            else:
                print('页面请求状态码：', response.status_code)
                return None
        except:
            print('在获取页面内容时出现错误：', response.status_code)
            # 向工作日志中写入内容
            return None

    # 提炼页面内容，返回列表内容
    def _extract(self, Info):
        # 返回值
        _list = {}

        # 采集表格中的数据
        _h = []

        for i in Info.find_all('tr'):
            for j in i.find_all('td'):
                _h.append(j.text)

        if '演出时长' in _h:
            _list['演出时长'] = _h[_h.index('演出时长') + 1]

        if '演出语言' in _h:
            _list['演出语言'] = _h[_h.index('演出语言') + 1]

        if '演出字幕' in _h:
            _list['演出字幕'] = _h[_h.index('演出字幕') + 1]

        if '主演演员（团体）' in _h:
            _list['主演演员（团体）'] = _h[_h.index('主演演员（团体）') + 1]

        for i in Info.find_all('div', class_='pre'):
            if i.find('演出介绍', beg=0, end=len(i)) != -1:
                _list['演出介绍'] = str(i.contents)

        _list['信息属性'] = self.steps

        return _list


if __name__ == '__main__':
    _i = get_show_list().get_value
