# -*- coding:utf-8 -*-
# 抄录员，用来将数据写入到数据库
import pandas as pd
import os
import pymongo

# import config  # 载入配置文件

# 获得当前路径的上级路径
curPath = os.path.dirname(os.getcwd())


# 输入数据，去重后保存到数据表，并返回需要查询到部分，已经查询过到部分，则会保存到日志
class entry_show_list:
    def __init__(self, List):
        # 数据库
        self.data_table = pymongo.MongoClient('mongodb://localhost:27017/')["swarm"]['show_list']

        self.data_list = List

        self._value = []  # 设置返回值

    @property
    def main(self):
        self._do()
        print('新增 %s 条演出信息' % len(self._value))
        return self._value

    def _do(self):

        for i in self.data_list:
            # print(bool(i['剧名']), bool(self.data_table.find_one({"剧名": i['剧名']})))

            # 如果剧名中有内容，则用剧名在数据库中查找
            if i['剧名']:
                # 如果数据库中有这个剧的内容，则进一步判断是否是同一个戏在不同的时间或场地演出
                if self.data_table.find_one({"剧名": i['剧名']}):
                    # 默认不存在此演出
                    _exist = False

                    # 是否能在剧名相同到内容中找到相同剧场和时间到内容，如果有，则代表是这个戏
                    for j in self.data_table.find({"剧名": i['剧名']}):
                        if i['演出场所'] == j['演出场所'] and i['演出时间'] == j['演出时间']:
                            _exist = True
                            print('此演出是重复到：', i['剧名'])

                    # 如果不存在，则代表，此剧再次演出
                    if not _exist:
                        # 保存内容
                        self.data_table.insert(i)
                        self._value.append(i)
                        print('此演出有多个演出场次：', i['剧名'])
                # 如果没有找到，则保存内容
                else:
                    self.data_table.insert(i)
                    self._value.append(i)
                    print('此演出是新增演出：', i['剧名'])

            # 如果剧名中没有内容，则用标题在数据库中查找
            else:
                # 如果数据库中有这个剧的内容，则进一步判断是否是同一个戏在不同的时间或场地演出
                if self.data_table.find_one({"标题": i['标题']}):
                    # 默认不存在此演出
                    _exist = False

                    # 是否能在剧名相同到内容中找到相同剧场和时间到内容，如果有，则代表是这个戏
                    for j in self.data_table.find({"标题": i['标题']}):
                        if i['演出场所'] == j['演出场所'] and i['演出时间'] == j['演出时间']:
                            _exist = True
                            print('此演出是重复到：', i['标题'])

                    # 如果不存在，则代表，此剧再次演出
                    if not _exist:  # 保存内容

                        self.data_table.insert(i)
                        self._value.append(i)
                        print('此演出有多个演出场次：', i['标题'])
                # 如果没有找到，则保存内容
                else:
                    self.data_table.insert(i)
                    self._value.append(i)
                    print('此演出是新增演出：', i['标题'])


class entry_review_list:
    def __init__(self, List):
        # 数据库
        self.data_table = pymongo.MongoClient('mongodb://localhost:27017/')["swarm"]['show_list']

        self.data_list = List

        self._value = []  # 设置返回值

    # 在大麦中获取内容的更详细信息
    def update_list(self, listName='info_drama.csv', headers='https://piao.damai.cn/'):
        _list = pd.DataFrame(pd.read_csv("res/" + listName, header=0, encoding='utf-8'))  # 读取CSV，以后是读取数据库

        for n, i in _list.iterrows():
            if i['信息属性'] == 0:  # 如果信息属性为0，则表示没有从大麦中获取数据，
                end = headers + str(i['projectid']) + '.html'
                get_info(end)

        # 更新列表中的内容，让他们更详细
        # 将超出时间的内容放在另一张表中，可以晚点做
        pass


if __name__ == '__main__':
    # csv_to_data()

    update_list()
    # print(curPath)
