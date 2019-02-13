# -*- coding: UTF-8 -*-
"""
作用：
用于被get_show调用，在get_show传入info

工作内容：
1. 完成提取ID，并抓取index页面的内容
2. 抓取XHR中的演出时间和票价信息，如果是多演出日期，则被分成几条内容
3. 在数据库中查重，并保存在数据库中

目前的问题：
1. 有的页面无法提取到XHR，这将导致数据提取不全面，我们将考虑用chorm方法来解决这个问题
"""
# 在大麦中到演出详情中，补全所有信息属性为0的活动的信息

# 公共库
import user_agent  # 随机生成user_agent
import time
import requests  # 加载解析地址库
import pymongo  # 数据库 应该挪到别的地方
import re  # 正则表达式
import json  # 解析json

# 内部库
from worker.readers.pretender import proxy  # 获取代理IP
from worker.toolkit import input_log  # 导入日志工具


class _get_info:
    def __init__(self, _info):
        self._info = _info
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "Cookie": 'isg=BGtrOki8s_nRIeqnNdE3_t-X-IlVgH8CnptDkN3p5KoBfIveZVIQUrQX0jwSx9f6; l=bBjEgDEuvr8wh-PKBOfBhurza779VId04kPzaNbMiICP9n565jihWZNgolLBC31Vw69HR3kZFxV_BeYBcX5..; x5sec=7b226d65632d67756964652d7765623b32223a223938666239626163336462386638663432623161336566323331383434353265434b6a78724f4946454b626f6d503270344e332b7251453d227d; _uab_collina=154843293526273207850894; destCity=%u6B66%u6C49; UM_distinctid=168417df3a2542-083e094567ce478-152f6841-13c680-168417df3a37ca; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%22168417df3a2542-083e094567ce478-152f6841-13c680-168417df3a37ca%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D%2C%22initial_view_time%22%3A%20%221547282679%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; x_hm_tuid=uLeWzJWLzMLkxF0RGLigKC8FopORbk+kAbriMBsYDnbgOkC3+iNHdnMAY+j0BglP; cna=W5Y0EQTl42YCARsRRUVaKCov',
            "referer": 'https://search.damai.cn/search.htm'
        }

        self.data_table = pymongo.MongoClient('mongodb://localhost:27017/')["swarm"]['show_list']  # 数据库

    def _get_url(self):  # 解析信息中的内容，使之变成可以访问的地址
        _long = len(str(self._info['projectid']))
        if _long == 6:
            _url = 'https://piao.damai.cn/%s.html' % self._info['projectid']
            return _url
        elif _long == 12:
            _url = 'https://detail.damai.cn/item.htm?id=%s' % self._info['projectid']
            return _url

    def _parse(self):  # 获取页面内容
        print('开始：%s ===> %s' % (__name__, self._parse.__name__))

        proxy_dict = {"http": ''}  # 这里需要制造代理,放这里，这样初始化的时候不需要马上执行这个方法

        _url = self._get_url()
        print(_url)
        try:
            _response = requests.get(url=_url, headers=self.headers, proxies=proxy_dict,
                                     verify=True)  # 获取get数据包,verify是否验证服务器的SSL证书

            if _response.status_code == 200:
                _response.encoding = 'UTF-8'  # 自行转码

                input_log(self._parse.__name__, '返回值', _response.text)  # 写入日志

                print('完成：%s ===> %s' % (__name__, self._parse.__name__))
                print()
                return _response.text  # 解析内容
            else:
                print('页面请求状态码：', _response.status_code)
                print('解析失败的URL：', self._get_url)
                exit()
        except Exception as e:
            print('解析失败：%s ===> %s' % (e, self._parse.__name__))
            exit()

    def _extract(self):  # 提炼页面内容，返回列表内容
        print('开始：%s ===> %s' % (__name__, self._extract.__name__))

        _home_page = self._parse()
        _list = {}  # 返回值

        # with open('../res/111', 'r') as file:
        #     _home_page = file.read()

        _title = _get_title(_home_page)  # 提取标题
        _venue = _get_venue(_home_page)  # 演出场馆
        _show_time = _get_show_time(_home_page)  # 演出时长
        _subtitle = _get_subtitle(_home_page)  # 有无中文字幕
        _language = _get_language(_home_page)  # 演出语言
        _show_team = _get_show_team(_home_page)  # 主演演员（团体）
        _briefing = _get_briefing(_home_page)  # 演出介绍

        _xhr = self._get_xhr()  # 获取异步内容
        if _xhr['Status']==200:
            print(_xhr)
            _start_time = _xhr['Data']['performs']  # 提取演出时间
            print(_start_time)
            _fare = _xhr['Data']['prices']  # 提取票价
            print(_fare)
        else:
            _start_time = list()  # 提取演出时间
            _fare = list()   # 提取票价
            print(_home_page)

    #
    # def main(self):  # 获取满足属性条件都所有信息的列表
    #     self._parse()
    #     # 获取属性值为0的内容
    #     info_list = self.data_table.find({'信息属性': 0})
    #
    #     # 逐个查询
    #     for i in info_list:
    #         _url = self._url_header + str(i['projectid']) + '.html'  # 拼接查询地址
    #         # print(_url)
    #
    #         _get_info = self._get_info(_url)  # 获取源代码
    #
    #         updata_data = self._extract(_get_info)  # 获取有用信息list
    #         # print('返回内容：',updata_data)
    #
    #         # 更新内容
    #         self.data_table.update({'projectid': i['projectid']}, {'$set': updata_data})
    #         print('完成更新 %s' % i['标题'])
    #         time.sleep(5)  # 设置5秒定时，避免反爬

    def _get_xhr(self):  # 获取页面内容
        print('开始：%s ===> %s' % (__name__, self._get_xhr.__name__))

        proxy_dict = {"http": ''}  # 这里需要制造代理,放这里，这样初始化的时候不需要马上执行这个方法
        _url = 'https://piao.damai.cn/ajax/getInfo.html?projectId=%s' % self._info['projectid']
        try:
            _response = requests.get(url=_url, headers=self.headers, proxies=proxy_dict,
                                     verify=True)  # 获取get数据包,verify是否验证服务器的SSL证书

            if _response.status_code == 200:
                _dict_data = json.loads(_response.text)  # 将字符串数据转换成字典数据，
                return _dict_data
            else:
                print('页面请求状态码：', _response.status_code)
                print('解析失败的URL：', _url)
                exit()
        except Exception as e:
            print('解析失败：%s ===> %s' % (e, self._get_xhr.__name__))
            exit()

    def _get_start_time_and_fare(self):  # 提取演出时间&演出票价
        print("演出时间", end='_')

        # _json = self._get_xhr()
        _json = """{"Status": 200, "Data": {"performs": [
            {"ProjectID": 173925, "PerformID": 9133673, "StartTime": "\/Date(1555587000000)\/",
             "PerformName": "2019-04-18 19:30:00", "MaxBuyCount": 20, "ShowDate": "2019.04.18", "ShowTime": "19:30",
             "ShowWeekday": "周四", "SeatBuyNum": 6, "Status": 1},
            {"ProjectID": 173925, "PerformID": 9133698, "StartTime": "\/Date(1555673400000)\/",
             "PerformName": "2019-04-19 19:30:00", "MaxBuyCount": 20, "ShowDate": "2019.04.19", "ShowTime": "19:30",
             "ShowWeekday": "周五", "SeatBuyNum": 6, "Status": 1},
            {"ProjectID": 173925, "PerformID": 9133700, "StartTime": "\/Date(1555741800000)\/",
             "PerformName": "2019-04-20 14:30:00", "MaxBuyCount": 20, "ShowDate": "2019.04.20", "ShowTime": "14:30",
             "ShowWeekday": "周六", "SeatBuyNum": 6, "Status": 1},
            {"ProjectID": 173925, "PerformID": 9133701, "StartTime": "\/Date(1555759800000)\/",
             "PerformName": "2019-04-20 19:30:00", "MaxBuyCount": 20, "ShowDate": "2019.04.20", "ShowTime": "19:30",
             "ShowWeekday": "周六", "SeatBuyNum": 6, "Status": 1}], "prices": [
            {"PriceID": 12658844, "PriceName": "100（G）", "SellPrice": 100.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658851, "PriceName": "150元（100（G）2张）", "SellPrice": 150.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658845, "PriceName": "180（F）", "SellPrice": 180.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658854, "PriceName": "230元（180（F）2张）", "SellPrice": 230.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658841, "PriceName": "280（E）", "SellPrice": 280.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658852, "PriceName": "330元（280（E）2张）", "SellPrice": 330.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658842, "PriceName": "380（D）", "SellPrice": 380.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658848, "PriceName": "430元（380（D）2张）", "SellPrice": 430.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658847, "PriceName": "480（C）", "SellPrice": 480.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658849, "PriceName": "530元（480（C）2张）", "SellPrice": 530.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658843, "PriceName": "680（B）", "SellPrice": 680.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658853, "PriceName": "730元（680（B）2张）", "SellPrice": 730.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false},
            {"PriceID": 12658846, "PriceName": "880（A）", "SellPrice": 880.00, "Status": 0, "IsTaoPiao": false,
             "IsAppPrice": false},
            {"PriceID": 12658850, "PriceName": "930元（880（A）2张）", "SellPrice": 930.00, "Status": 0, "IsTaoPiao": true,
             "IsAppPrice": false}], "performId": 9133673, "ele": true, "xz": true, "b3": false, "saleStatus": 1},
                 "Message": null}"""
        _json = json.loads(_json)

        # _start_time = re.findall(r'演出时间：(.*?)<span>(.*?)</span>', _info, re.S)
        print(_json['Data'])
        # print(_fare)

        return _json


def _get_title(_info):  # 提取标题
    print("标题", end='_')

    while True:
        _re = re.findall(r'"m-goods"(.*?)"txt">(.*?)</span>', _info, re.S)  # 方案A，用于有项目模块的类型
        if _re:
            _title = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'"perform__order"(.*?)<div(.*?)>(.*?)</div>', _info, re.S)  # 方案B，用用没有项目模块的类型
        if _re:
            _title = _re[0][-1]
            print("方案A", end='\t')
            break
        _title = []
        print("未搜到:%s" % _re, end='\t')
        break

    print(_title)
    return _title


def _get_venue(_info):  # 提取演出场地
    print("演出场地", end='_')

    while True:
        _re = re.findall(r'演出时间：(.*?)<span>(.*?)</span>', _info, re.S)  # 方案A
        if _re:
            _venue = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'"venueName":"(.*?)"', _info, re.S)  # 方案B#查找不到演出场地时，使用此方案
        if _re:
            _venue = _re[0]
            print("方案B", end='\t')
            break

        _venue = ''  # 未搜到
        print("未搜到:%s" % _re, end='\t')
        break

    print(_venue)
    return _venue


def _get_show_time(_info):  # 提取演出时长
    print("演出时长", end='_')

    while True:
        _re = re.findall(r'演出时长：(.*?)<span>(.*?)</span>', _info, re.S)  # 方案A
        # print(_re, end='\t')
        if _re:
            _show_time = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'演出时长</p>(.*?)<li>(.*?)</li>', _info, re.S)  # 方案B，没有写在表格中，写在演出介绍中的内容
        # print(_re, end='\t')
        if _re:
            _show_time = _re[0][-1]
            print("方案B", end='\t')
            break

        _show_time = ''  # 未搜到
        print("未搜到:%s" % _re, end='\t')
        break

    print(_show_time)
    return _show_time


def _get_subtitle(_info):  # 提取有无中文字幕
    print("中文字幕", end='_')

    while True:
        _re = re.findall(r'有无中文字幕</td>(.*?)<td>(.*?)</td>', _info, re.S)  # 方案A
        if _re:
            _subtitle = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'有无中文字幕</td>(.*?)<td>(.*?)</td>', _info, re.S)  # 方案B
        if _re:
            _subtitle = _re[0]
            print("方案B", end='\t')
            break

        _subtitle = ''  # 如果没有相关信息
        print("未搜到:%s" % _re, end='\t')
        break

    print(_subtitle)
    return _subtitle


def _get_language(_info):  # 提取演出语言
    print("演出语言", end='_')

    while True:
        _re = re.findall(r'演出语言</td>(.*?)<td>(.*?)</td>', _info, re.S)  # 方案A
        if _re:
            _language = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'演出语言</td>(.*?)<td>(.*?)</td>', _info, re.S)  # 方案B
        if _re:
            _language = _re[0]
            print("方案B", end='\t')
            break

        _language = ''  # 如果没有相关信息
        print("未搜到:%s" % _re, end='\t')
        break

    print(_language)
    return _language


def _get_show_team(_info):  # 提取演出团队
    print("演出团队", end='_')

    while True:
        _re = re.findall(r'主要演员(.*?)<td>(.*?)<', _info, re.S)  # 方案A
        if _re:
            _show_team = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'主要演员(.*?)<li>(.*?)<', _info, re.S)  # 方案B，没有写在表格中，写在演出介绍中时
        if _re:
            _show_team = _re[0][-1]
            print("方案B", end='\t')
            break

        _show_team = []
        print("未搜到:%s" % _re, end='\t')
        break

    print(_show_team)
    return _show_team


def _get_briefing(_info):  # 提取演出介绍
    print("演出介绍", end='_')

    while True:
        _re = re.findall(r'"infoitm"(.*?)</dl>', _info, re.S)  # 方案A
        # print(_re, end='_')
        if _re:
            _start_time = _re[0][-1]
            print("方案A", end='\t')
            break

        _re = re.findall(r'演出介绍(.*?)perform__bd__words">(.*?)</div>', _info, re.S)  # 方案B
        # print(_re, end='_')
        if _re:
            _start_time = _re[0][-1]
            print("方案B", end='\t')
            break

        _start_time = []
        print("未搜到:%s" % _re, end='\t')
        break

    print(_start_time)
    return _start_time


def main(_info):  # 如果是一个时间，则是同步显示，如果是多天，则是异步
    b = _get_info(_info)
    b._extract()


if __name__ == '__main__':
    main({'name': '开心麻花爆笑舞台剧《牢友记》武汉站', 'theatre': '武汉琴台大剧院', 'showtime': '2019.10.23 周三', 'state': '售票中',
          'projectid': 586701999767, 'read': False})
    # main({'name': '开心麻花2019爆笑贺岁舞台剧《疯狂双子星》', 'theatre': '湖北剧院', 'showtime': '2019.04.18-04.20', 'state': '售票中',
    #       'projectid': 173925, 'read': False})
