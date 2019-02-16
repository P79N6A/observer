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
from selenium import webdriver  # 浏览器驱动
import sys
import os  # 转换内容 ，并提取数据

# 内部库
from worker.readers.pretender import proxy  # 获取代理IP
from worker.toolkit import input_log  # 导入日志工具


def _get_url(_info):
    """
    解析信息中的内容，使之变成可以访问的地址
    :param _info: {'name': '武汉说唱团爆笑神剧《海底捞月》', 'theatre': '汤湖戏院', 'showtime': '2018.12.29-2019.02.19', 'state': '售票中', 'projectid': 169619, 'read': False}
    :return: url
    """
    _name = sys._getframe().f_code.co_name
    print('开始生成地址：%s' % _name)
    _long = len(str(_info['projectid']))
    if _long == 6:
        _url = 'https://piao.damai.cn/%s.html' % _info['projectid']
    elif _long == 12:
        _url = 'https://detail.damai.cn/item.htm?id=%s' % _info['projectid']
    else:
        print('无法从演出信息中解析出url：%s' % _info)
        _url = ''
        exit()

    print('生成地址：%s' % _url)
    return _url


def _get_title(_home_page):
    """
    提取标题
    :param _home_page:
    :return:
    """
    print("标题", end='_')

    while True:
        _re_A = re.findall(r'"Name":"(.*?)"', _home_page, re.S)  # 方案A，用于有项目模块的类型
        if _re_A:
            _title = _re_A[0]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'"perform__order"(.*?)<div(.*?)>(.*?)</div>', _home_page, re.S)  # 方案B，用用没有项目模块的类型
        if _re_B:
            _title = _re_B[0][-1]
            print("方案A", end='\t')
            break

        _title = []
        print("未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    print(_title)
    return _title


def _get_venue(_home_page):
    """
    提取演出场地
    :param _home_page:
    :return:
    """
    print("演出场地", end='_')

    while True:
        _re_A = re.findall(r'VenueName":"(.*?)"', _home_page, re.S)  # 方案A
        if _re_A:
            _venue = _re_A[0]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'演出时间：(.*?)<span>(.*?)</span>', _home_page, re.S)  # 方案B#查找不到演出场地时，使用此方案
        if _re_B:
            _venue = _re_B[0]
            print("方案B", end='\t')
            break

        _venue = []
        print("未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    print(_venue)
    return _venue


def _get_start_date(_home_page):
    """
    获取演出时间
    :return: list，包含所有时间
    """
    print('演出时间', end='_')
    while True:
        _re_A = re.findall(r'data-performtime="(.*?)"', _home_page, re.S)  # 方案A，在xhr中的类型
        if _re_A:
            _start_date = list()
            for i in _re_A:
                _start_date.append(i)
            print("方案A:%s" % _start_date)
            break

        _re_B = re.findall(r'dataDefault(.*?)performName":"(.*?)","', _home_page, re.S)  # 方案B，没有写在表格中，写在演出介绍中时
        if _re_B:
            _start_date = _re_B[0][-1]
            print("方案B:%s" % _start_date)
            break

        _start_date = []
        print("未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    return _start_date


def _get_price(_home_page):
    """
    获取票价
    :param _home_page:
    :return:
    """
    while True:
        _re_A = re.findall(r'data-price="(.*?)"', _home_page, re.S)  # 方案A，在xhr中的类型
        if _re_A:
            _price = list()
            for i in _re_A:
                _price.append(i)
            print("票价_方案A:%s" % _re_A)
            break

        _re_B = re.findall(r'dashPrice(.*?)price":(.*?),', _home_page, re.S)  # 方案B，没有写在表格中，写在演出介绍中时
        if _re_B:
            _price = list()
            for i in _re_B:
                _price.append(int(i[-1]))
            print("票价_方案B:%s" % _price)
            break

        _price = []
        print("票价_未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    return _price


def _get_show_time(_home_page):
    """
    提取演出时长
    :param _home_page:
    :return:
    """
    print("演出时长", end='_')

    while True:
        _re_A = re.findall(r'演出时长(.*?)<span>(.*?)</span>', _home_page, re.S)  # 方案A
        if len(_re_A)>3:
            _show_time = _re_A[0][-1]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'演出时长</p>(.*?)<li>(.*?)</li>', _home_page, re.S)  # 方案B，没有写在表格中，写在演出介绍中的内容
        if _re_B:
            _show_time = _re_B[0][-1]
            print("方案B", end='\t')
            break
        _re_C = re.findall(r'演出时长(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案C，没有写在表格中，写在演出介绍中的内容
        if _re_C:
            _show_time = _re_C[0][-1]
            print("方案C", end='\t')
            break

        _show_time = ''  # 未搜到
        print("未搜到\n方案A:%s\n方案B:%s\n方案C:%s" % (_re_A, _re_B,_re_C))
        break

    print(_show_time)
    return _show_time


def _get_subtitle(_home_page):
    """
    提取有无中文字幕
    :param _home_page:
    :return:
    """
    print("中文字幕", end='_')

    while True:
        _re_A = re.findall(r'有无中文字幕</td>(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案A
        if _re_A:
            _subtitle = _re_A[0][-1]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'有无中文字幕</td>(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案B
        if _re_B:
            _subtitle = _re_B[0]
            print("方案B", end='\t')
            break

        _subtitle = ''  # 如果没有相关信息
        print("票价_未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    print(_subtitle)
    return _subtitle


def _get_language(_home_page):
    """
    提取演出语言
    :param _home_page:
    :return:
    """
    print("演出语言", end='_')

    while True:
        _re_A = re.findall(r'演出语言</td>(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案A
        if _re_A:
            _language = _re_A[0][-1]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'演出语言</td>(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案B
        if _re_B:
            _language = _re_B[0]
            print("方案B", end='\t')
            break

        _language = ''  # 如果没有相关信息
        print("票价_未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    print(_language)
    return _language


def _get_show_team(_home_page):
    """
    提取演出团队
    :param _home_page:
    :return:
    """
    print("演出团队", end='_')

    while True:
        _re_A = re.findall(r'主要演员(.*?)<td>(.*?)</td>', _home_page, re.S)  # 方案A
        if _re_A:
            _show_team = _re_A[0][-1]
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'主要演员(.*?)<li>(.*?)<', _home_page, re.S)  # 方案B，没有写在表格中，写在演出介绍中时
        if _re_B:
            _show_team = _re_B[0][-1]
            print("方案B", end='\t')
            break

        _re_C = re.findall(r'主演演员(.*?)<td>(.*?)<br>', _home_page, re.S)  # 方案C，有的写成了主演演员
        if _re_C:
            _show_team = _re_C[0][-1]
            print("方案C", end='\t')
            break

        _show_team = ''
        print("未搜到\n方案A:%s\n方案B:%s\n方案C:%s" % (_re_A, _re_B,_re_C))
        break

    print(_show_team)
    return _show_team


def _get_briefing(_home_page):
    """
    提取演出介绍
    :param _home_page:
    :return:
    """
    print("演出介绍", end='_')

    while True:
        _re_A = re.findall(r'项目介绍(.*?)pre">(.*?)</div>', _home_page, re.S)  # 方案A
        if _re_A:
            _start_time = _re_A[0][-1].replace('\n', '')
            print("方案A", end='\t')
            break

        _re_B = re.findall(r'演出介绍(.*?)perform__bd__words">(.*?)</div>', _home_page, re.S)  # 方案B
        if _re_B:
            _start_time = _re_B[0][-1].replace('\n', '')
            print("方案B", end='\t')
            break

        _start_time = []
        print("未搜到\n方案A:%s\n方案B:%s" % (_re_A, _re_B))
        break

    print(_start_time)
    return _start_time


def _get_info(_home_page):
    """
    根据不同的html内容，分为两种解析方案，提取有用的信息
    :param html:
    :return:
    """
    _name = sys._getframe().f_code.co_name
    print('开始解析页面信息：%s' % _name)

    _list_info = list()  # 返回值，不同到演出日期，单独一条信息
    # with open('%s/res/222' % os.path.dirname(os.getcwd()), 'r') as file:
    #     _home_page = file.read()

    _title = _get_title(_home_page)  # 提取标题
    _venue = _get_venue(_home_page)  # 演出场馆
    _start_date = _get_start_date(_home_page)  # 演出日期
    _price = _get_price(_home_page)  # 票价
    _show_time = _get_show_time(_home_page)  # 演出时长
    _subtitle = _get_subtitle(_home_page)  # 有无中文字幕
    _language = _get_language(_home_page)  # 演出语言
    _show_team = _get_show_team(_home_page)  # 主演演员（团体）
    _briefing = _get_briefing(_home_page)  # 演出介绍

    for i in _start_date:
        _i = dict(标题=_title, 演出场馆=_venue, 演出日期=i, 票价=_price, 演出时长=_show_time, 有无中文字幕=_subtitle, 演出语言=_language,
                  团体=_show_team, 演出介绍=_briefing)  # 返回值，字典
        _list_info.append(_i)

    input_log(_name, '提取制', _list_info)  # 写入日志

    print(_list_info)
    return _list_info


def _get_html(list_show):
    """
    启动Safari浏览器，访问url，获取页面信息
    :param _info: 从get_show传过来的单条演出信息。{'name': '武汉说唱团爆笑神剧《海底捞月》', 'theatre': '汤湖戏院', 'showtime': '2018.12.29-2019.02.19', 'state': '售票中', 'projectid': 169619, 'read': False}
    :return: 页面信息
    """
    _name = sys._getframe().f_code.co_name
    print('开始获取页面信息：%s' % _name)

    _list_get_show = list()  # 返回值

    browser = webdriver.Safari()  # 启动Safari浏览器

    _v = 0
    for i in list_show:
        if not i['read']:  # 如果状态是False，则获取信息
            print('将要抓取的戏的信息：%s' % i)
            _url = _get_url(i)
            browser.get(_url)  # 获取页面信息
            _home_page = browser.page_source
            input_log(_name, 'html', _home_page)  # 写入日志
            _info = _get_info(_home_page)
            _list_get_show += _info  # 因为_info也是列表，所以直接加了

    print(_list_get_show)
    return _list_get_show


def main(list_show):  # 如果是一个时间，则是同步显示，如果是多天，则是异步
    list_get_info = _get_html(list_show)
    #放到数据库里查询并保存


if __name__ == '__main__':
    main([{'name': '开心麻花2019爆笑贺岁舞台剧《疯狂双子星》', 'theatre': '湖北剧院', 'showtime': '2019.04.18-04.20', 'state': '售票中', 'projectid': 173925, 'read': False}])
