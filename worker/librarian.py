# -*- coding: UTF-8 -*-
"""
图书管理员，用来从数据库调取资料
"""
# 公共库
from pymongo import MongoClient  # 操作数据库
from datetime import datetime  # 获取时间

settings = {"ip": 'mongodb://localhost',  # ip
            "port": 27017,  # 端口
            "db_name": "swarm",  # 数据库名字
            "set_name": "show_list"  # 集合名字
            }
db_data = MongoClient(settings["ip"], settings["port"])
mydb = db_data[settings["db_name"]]
my_set = mydb[settings["set_name"]]

_now = datetime.now().date()


def get_show(days=7):
    """
    作用：
    获取从今日起7天的演出数据
    如果7日内没有演出数据，则获取14日内演出数据，如果14日内没有数据，则获取1个月的演出数据，如果依然没有，则返回"无演出"
    :return:
    """
    _list_day_7 = list()
    _list_day_14 = list()
    _list_day_31 = list()

    for i in my_set.find():
        _time = datetime.strptime(i['演出时间'][:10], "%Y.%m.%d").date()
        _t = (_time - _now).days
        print(_t)
        if 0 <= _t:  # 提取符合要求的时间，并加入到对应列表中
            if _t <= 7:
                _list_day_7.append(i)
                _list_day_14.append(i)
                _list_day_31.append(i)
            elif _t <= 14:
                _list_day_14.append(i)
                _list_day_31.append(i)
            elif _t <= 31:
                _list_day_31.append(i)
            else:
                pass

    if days == 7:
        if len(_list_day_7) != 0:
            txt = ''
            _v = 0
            for i in _list_day_7:
                _v += 1
                txt += '\n\n%s. 剧目：%s\n演出时间：%s\n演出场地：%s' % (_v,i['标题'], i['演出时间'], i['演出场所'])
            return '最近1周内演出信息:%s' % txt
        else:
            return '最近1周内没有演出信息'
    elif days == 14:
        if len(_list_day_14) != 0:
            txt = ''
            _v = 0
            for i in _list_day_7:
                _v += 1
                txt += '\r%s. 剧目：%s，演出时间：%s，演出场地：%s' % (_v,i['标题'], i['演出时间'], i['演出场所'])
            return '最近两周内演出信息:%s' % txt
        else:
            return '最近两周内没有演出信息'
    elif days == 31:
        if len(_list_day_14) != 0:
            txt = ''
            _v = 0
            for i in _list_day_7:
                _v += 1
                txt += '\r%s. 剧目：%s，演出时间：%s，演出场地：%s' % (_v, i['标题'], i['演出时间'], i['演出场所'])
            return '最近1个月内演出信息:%s' % txt
        else:
            return '最近1个月内没有演出信息'


if __name__ == '__main__':
    print(get_show(31))
