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
from worker.readers import douban_diary


# 搜索关键词，得到相关信息都连接
class get_review:
    def __init__(self, word):
        self.word = word  # 关键词

        self.URL_Headers = 'https://www.baidu.com/s?ie=UTF-8&wd='  # 地址头
        self.headers = {"User-Agent": user_agent.generate_user_agent()}  # 随机生成的
        self.proxy_dict = {"http": proxy().get_one}  # 这里需要制造代理

        self.pages = 5  # 单个剧目在百度搜索的页数

        self.query_times = 1  # 查询剧目的条数

        self.steps = 2  # 步骤参数

    # 返回页面的源代码,会因为反爬虫，所以需要额外做判断，之后要把这部分单独做出来
    def _get_parse(self, path):
        try:
            _response = requests.get(path, headers=self.headers)
            if _response.status_code == 200:
                # 自行转码
                _response.encoding = 'UTF-8'
                # 解析内容
                page_source = BS(_response.text, 'html.parser')

                # print('搜索完成:%s' % self.word)
                time.sleep(3)
                return page_source
            else:
                print(_response.status_code)
                return
        except RequestException:
            # 向工作日志中写入内容
            return

    # 提取代码中的地址，并返回搜索结果的真实地址列表
    @property
    def _get_list(self):
        if os.path.exists('../res/list_%s.txt' % self.word):  # 是否存在list版，存在则读取内容
            print('运气很好，有对应的list文件，开始读取……')
            _file = open('../res/list_%s.txt' % self.word, 'r', encoding='utf-8').read()
            _list = eval(_file)

            # print('读取成功：res/%s_mini.txt' % _list)
            return _list
        else:  # 没有文件，则自己生产吧
            _list = []  # 返回值

            # 逐个页面搜索
            for i_pages in range(self.pages):
                print('开始搜索第%d页' % (i_pages + 1))
                # 拼接页面地址
                if i_pages == 0:
                    search_url = '%s%s' % (self.URL_Headers, self.word)
                else:
                    search_url = '%s%s&pn=%s' % (self.URL_Headers, self.word, i_pages * 10)
                # print('搜索地址：%s'% search_url)

                parse = self._get_parse(search_url)  # 获取百度代码
                _data = parse.find_all('h3', class_='t')  # 提取搜索结果区域

                # 逐个提取地址，并添加到_list
                for i in _data:
                    _href = str(i.find('a').get('href'))
                    # print(_href)

                    # 百度重定向到问题暂时解决不了，只能自己保存内容了
                    with requests.get(_href, allow_redirects=True) as _response:
                        # print(_response.url)
                        # print(_response.text)
                        if _response.url not in _list:  # 去重
                            _list.append(_response.url)

                print('添加地址:%s' % len(_data))
                time.sleep(1)

            # 将内容保存在test ！可以考虑把这个部分提前，这样就算在中间有报错，也可以获取一定数量到内容
            with open('../res/list_%s.txt' % self.word,
                      'w+') as save_file:
                save_file.write(str(_list))
                print('成功保存：%s条' % len(_list))

            # print('提取完成：%s' % _list)
            return _list

    # 主函数
    def main(self):
        list = self._get_list  # 提取需要采集到网址列表

        self.fenjian(list)

    # 将传入的列表中的地址分类，并调用对应的函数来处理，最后返回数据库_id列表
    def fenjian(self, list):
        id_list = []  # 保存_id
        douban = []
        sohu = []
        qita = []

        for i in list:
            _id = self.dddd(i)
            id_list.append(_id)

    # 将地址分拣，调用对应的函数，在处理后，返回_id 或空值
    def dddd(self, i):
        # 分拣地址
        netloc = urlparse(i).netloc  # 解析URL
        if netloc == 'www.douban.com':  # 地址来源：豆瓣
            path = urlparse(i).path.split('/')

            if path[1] == 'event':  # 地址来源：豆瓣-同城活动
                # print('豆瓣-同城活动：%s' % i)
                pass
            elif path[1] == 'group':  # 地址来源：豆瓣-豆瓣小组
                # print('豆瓣-豆瓣小组：%s' % i)
                pass
            elif path[1] == 'note':  # 地址来源：豆瓣-豆瓣日记
                print('豆瓣-豆瓣日记：%s' % i)
                return douban_diary(i)  # 获取返回的ID，最后和原帖相关联
            elif path[1] == 'location':
                if path[2] == 'drama':  # 地址来源：豆瓣-舞台剧活动-首页
                    # print('豆瓣-舞台剧活动-首页：%s' % i)
                    pass
                elif path[3] == 'review':  # 地址来源：豆瓣-舞台剧活动-长文评论
                    # print('豆瓣-舞台剧活动-长文评论：%s' % i)
                    pass
                elif path[4] == 'comments':  # 地址来源：豆瓣-舞台剧活动-短评
                    # print('豆瓣-舞台剧活动-短评：%s' % i)
                    pass

            douban.append(i)

        elif netloc == 'www.sohu.com':  # 是否为搜狐的内容
            # print('内容来源：搜狐：%s' % i)
            sohu.append(i)
            # 需要考虑内容去重的问题

        elif netloc == 'blog.sina.com.cn':  # 是否为新浪微博的内容
            # print('内容来源：新浪博客：%s' % i)
            sohu.append(i)
            # 需要考虑内容去重的问题

        else:  # 各种个样到内容
            # print('内容来源：其他：%s' % i)
            qita.append(i)

        # break
        # 输入到数据库
        # 添加到列表
        # 写入到对应到剧目中


if __name__ == '__main__':
    _i = get_review('杏仁豆腐心').main()
