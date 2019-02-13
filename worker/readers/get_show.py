# -*- coding: UTF-8 -*-
"""
作用：
用于被director调用，不需要任何参数

工作内容：
1. 在大麦中的演出列表的数据提取
2. 和本地的res/list_show文件中的内容进行对比，并保存新内容
3. 新内容调用get_info来抓取新的内容，通过get_info完成内容的抓取和保存到数据

目前到问题：
1. 目前问题都在get_info中
"""

# 公共库
import os  # 转换内容 ，并提取数据
import user_agent  # 随机生成user_agent
import time
import requests  # 加载解析地址库
import re
import json  # 解析json
from datetime import datetime  # 日期处理

# 内部库
from worker.readers.pretender import proxy  # 获取代理IP
from worker.toolkit import input_log  # 导入日志工具
from worker.readers.get_info import main as get_info

_path = 'res/list_show'  # 这个文件是用户一共有哪些演出列表，类似现在数据库中到演出信息
_now = datetime.now()


class _get_show:
    def __init__(self):
        self.post_url = 'https://search.damai.cn/searchajax.html'  # 大麦网接受POST请求的地址

        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "Cookie": 'isg=BGtrOki8s_nRIeqnNdE3_t-X-IlVgH8CnptDkN3p5KoBfIveZVIQUrQX0jwSx9f6; l=bBjEgDEuvr8wh-PKBOfBhurza779VId04kPzaNbMiICP9n565jihWZNgolLBC31Vw69HR3kZFxV_BeYBcX5..; x5sec=7b226d65632d67756964652d7765623b32223a223938666239626163336462386638663432623161336566323331383434353265434b6a78724f4946454b626f6d503270344e332b7251453d227d; _uab_collina=154843293526273207850894; destCity=%u6B66%u6C49; UM_distinctid=168417df3a2542-083e094567ce478-152f6841-13c680-168417df3a37ca; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%22168417df3a2542-083e094567ce478-152f6841-13c680-168417df3a37ca%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D%2C%22initial_view_time%22%3A%20%221547282679%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%7D; x_hm_tuid=uLeWzJWLzMLkxF0RGLigKC8FopORbk+kAbriMBsYDnbgOkC3+iNHdnMAY+j0BglP; cna=W5Y0EQTl42YCARsRRUVaKCov',
            "Referer": 'https://search.damai.cn/search.htm'
        }  # 请求头内容

        self.data = {"cty": "武汉", "ctl": "话剧歌剧", "tsg": "0", "order": "0"}  # 请求内容

        self.list_show = list()  # 需要遍历的演出列表

    def _parse(self):  # 解析页面
        print('开始解析：%s ===> %s' % (__name__, self._parse.__name__))
        _json = list()  # 返回值
        proxy_dict = {"http": proxy().get_one}  # 这里需要制造代理,放这里，这样初始化的时候不需要马上执行这个方法

        try:  # 如果被反扒，则解析json时会出错
            _response = requests.post(url=self.post_url, headers=self.headers, proxies=proxy_dict, data=self.data,
                                      verify=True)  # verify是否验证服务器的SSL证书)

            if _response.status_code == 200:
                input_log(self._parse.__name__, '返回值', _response.text)  # 写入日志

                _dict_data = json.loads(_response.text)  # 将字符串数据转换成字典数据，
                if 'rgv587_flag' not in _dict_data:  # 判断是否被反爬
                    _json = _dict_data["pageData"]["resultData"]

                    input_log(self._parse.__name__, '提取值', _json)  # 写入日志

                    print('完成解析：%s ===> %s' % (__name__, self._parse.__name__))
                    return _json  # 将需要的爬取的字典数据存储在变量中

                else:
                    print('被反爬了，目前因为不确定反爬方式，所以直接终止工作：%s ===> %s' % (__name__, self._parse.__name__))
                    exit()
            else:
                print('返回值异常：%s ===> %s' % (__name__, self._parse.__name__))
                exit()
        except Exception as e:
            print('解析失败：%s ===> %s' % (__name__, self._parse.__name__))
            exit()

    def _extract(self):  # 提取数据,返回提取到的所有演出信息列表
        print('开始提取数据：%s ===> %s' % (__name__, self._extract.__name__))
        _list_now = list()  # 返回值

        for _info in self._parse():  # 获取有用信息
            _j = {'name': _info['name'], 'theatre': _info['venue'], 'showtime': _info['showtime'],
                  'state': _info['showstatus'], 'projectid': _info['projectid'], 'read': False}  # 获取有用的信息,属性

            _list_now.append(_j)
            input_log(self._extract.__name__, _j)  # 写入日志

        with open(_path, 'w') as file:
            file.write(str(_list_now))

        return _list_now

    def _save(self):  # 带时间戳，把内容都保存到'res/list_show'中
        with open(_path, 'w') as file:  # 保存内容到文件
            file.write(_now.strftime('%Y-%m-%d %H:%M:%S'))  # 写入更新时间,保存的时候要处理下时间格式
            file.write('\n')
            file.write(str(self.list_show))

    def _get_list(self):  # 获取需要提取的演出内容,使得list_show可以用来遍历获取详细到演出信息
        print('开始提取list：%s ===> %s' % (__name__, self._get_list.__name__))

        if os.path.exists(_path):  # 如果有文件，则读取文件，并返回

            with open(_path, 'r') as file:
                _file = file.readlines()  # ['更新时间'，'演出数据']
                _update = datetime.strptime(_file[0].rstrip(), "%Y-%m-%d %H:%M:%S")  # 获取更新时间

            if (_now - _update).seconds > 36000 or (_now - _update).days > 0:  # 更新时间距离今天大于10小时，或者大于1天，则需要额外获取新演出信息
                print('有原文件，但已经过时：%s' % '新生成')
                self.list_show = eval(_file[1])
                _v = 0  # 新增数量
                for i in self._extract():
                    print(i)
                    if i not in self.list_show:  # 如果新演出信息在原文件中，则需要进一步解析
                        self.list_show.append(i)
                        _v += 1
                        input_log(self._extract.__name__, '添加', i)  # 写入日志

                    else:  # 如果在就不管
                        input_log(self._extract.__name__, '重复值', i)  # 写入日志

                    break
                print('添加新内容：%s' % _v)

                self._save()  # 保存self.list_show

            else:  # 则使用原文件，不更新
                print('%s' % '使用原文件，不再获取演出列表')
                self.list_show = eval(_file[1])

        else:  # 如果没有文件，则更新
            print('没有原文件，生成文件：%s' % _path)
            self.list_show = self._extract()

            self._save()  # 保存self.list_show

    def _get_show(self):  # 解析单个演出信息
        _v = 0
        for i in self.list_show:
            if not i['read']:  # 如果状态是False，则获取信息
                print('将要抓取的戏的信息%s' % i)
                get_info(i)  # 获取具体信息，并保存到数据库

            break


def main():
    a = _get_show()
    a._get_list()  # 生成self.list_show
    a._get_show()  # 调用get_info()获取单个信息

if __name__ == '__main__':
    main()