# -*- coding: UTF-8 -*-
##########################################
# 导演，控制目前所有的内容的完成，作为总控台，完成所有分配任务
##########################################

# from worker.writers import update_list   as update_list
from worker.readers import get_show_list, get_info
from worker.writers import entry_show_list


class controller(object):
    # 构造请求头等
    def __init__(self):
        # 大麦网接受POST请求的地址
        self.re = 'https://search.damai.cn/searchajax.html'

        # 第一次抓去之后，就可以放到这个里面了
        self.listName = 'info_drama.csv'

    # 主函数
    def to_do(self):
        _get_show_list = get_show_list().get_value  # 调用函数，获取演出:List

        _entry_show_list = entry_show_list(_get_show_list).get_value# 将列表中的信息写入数据库，写入时会进r行去重操作

        _get_info = get_info().updata()# 抓取更详细的内容，也是通过大麦

        # 抓取周边信息，通过百度，调用更多的爬虫


        # 通过文本分析，提取剧目对应的关键词，然后形成词云，展示出来
        # _get_list = get_url(self.re).todo()  # 解析演出列表页面，返回包含演出基本信息的数组   可以改变下思路，将这一步变成获取新的演出列表，把获取信息放在写入类中，让写入类调用阅读类
        # # print(_get_list)
        #
        # # 去重之后放到ListName这个文件中,是第一次获取数据，并返回去重后到数据
        # save_list(_get_list, self.listName)
        # print('更新了列表')

        # 更新列表中的内容，让内容更详细
        # update_list(self.listName, self._url_header)

        # 逐个地址获取演出的详细信息，将详细的信息添加进来，返回完整的DataFrame
        # _good_info = self.get_info()


if __name__ == '__main__':
    controller().to_do()
