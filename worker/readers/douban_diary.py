# -*- coding: UTF-8 -*-
# 豆瓣-豆瓣日记
# 公共库
import user_agent  # 随机生成user_agent
import time
import os  # 转换内容 ，并提取数据
import requests  # 加载解析地址库
from requests import RequestException  # try库
import re  # 正则表达式
import pymongo  # 操作数据库

# 内部库
from worker.readers.pretender import proxy  # 获取代理IP
from worker.toolkit import whether_repeat  # 工具


# 搜索关键词，得到相关信息都连接
class douban_diary:
    def __init__(self, url):
        self.url = url  # 关键词

        self.headers = {"User-Agent": user_agent.generate_user_agent()}  # 随机生成的
        self.proxy_dict = {"http": proxy().get_one}  # 这里需要制造代理

        self.value = []  # 返回值

    # 返回页面的源代码,会因为反爬虫，所以需要额外做判断，之后要把这部分单独做出来
    @property
    def _get_parse(self):
        try:
            _response = requests.get(self.url, headers=self.headers, proxies=self.proxy_dict)
            if _response.status_code == 200:
                # 自行转码
                _response.encoding = 'UTF-8'

                # print('搜索完成:%s' % self.word)
                return _response.text
            else:
                print(_response.status_code)
                return
        except RequestException:
            # 向工作日志中写入内容
            return

    # 获取有用信息
    def extract_data(self, parse):
        # step1=parse.find('div',class_='article')
        # # print(step1)

        # 提取标题
        _title = re.findall(r'note-header.*?<h1>(.*?)</h1>', parse, re.S)[0]
        # 提取作者名
        _author = re.findall(r'note-author.*?>(.*?)</a>', parse, re.S)[0]
        # 提取发布时间
        _date = re.findall(r'pub-date.*?>(.*?)</span>', parse, re.S)[0]
        # 正文
        _note = re.findall(r'\"link-report\".*?>(.*?)</div>', parse, re.S)[0]

        _data = (_title, _author, _date, _note)  # 标题、作者吗、发布时间、正文
        return _data

    # 写入数据，同时返回ID
    def entry_data(self, data):
        db_data = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = db_data.swarm
        my_set = mydb.review_list

        text_list = whether_repeat(db_data)  # 输入内容，如果数据库中不重复，则返回分词，重复则返回空值

        if text_list:  # 返回分析结果，说明可以保存
            _title = data[0]  # 标题
            _author = data[1]  # 作者名
            _date = data[2]  # 时间
            _note = data[3]  # 正文
            _label = text_list  # 分词

            data = {'title': _title, 'author': _author, 'date': _date, 'note': _note, 'label': _label, 'from': self.url}
            ggg = my_set.insert_one(data)  # 保存数据

            db_data.close()
            print(ggg.inserted_id)
            return ggg.inserted_id
        else:
            # 不写入
            return

    # 主函数
    def main(self):
        parse = self._get_parse  # 获取代码
        # print(parse)

        data = self.extract_data(parse)  # 提取有效内容 并返回列表

        data_id = self.entry_data(data)  # 查看数据库中的内容，如果没有 则放入数据库，返回ID

        return data_id


if __name__ == '__main__':
    text = 'https://www.douban.com/note/684388706/'
    _i = douban_diary(text).main()
