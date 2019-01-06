# -*- coding:utf-8 -*-
# 抄录员，用来将数据写入到数据库
import pandas as pd
import os
import pymongo

import config  # 载入配置文件

# 获得当前路径的上级路径
curPath = os.path.dirname(os.getcwd())

# 数据库地址
myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# 数据库名字
mydb = myclient["swarm"]


# 输入数据，去重后保存到数据表，并返回需要查询到部分，已经查询过到部分，则会保存到日志
class entry_show_list():
    # 构造请求头等
    def __init__(self, List):
        # 数据库
        self.data_table = mydb['show_list']

        self.data_list = List

        self._value=[]   #设置返回值
    @property
    def get_value(self):
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



# 把传入的列表中的内容和数据库中的内容做对比，去重并返回不重复的内容
def entry_list(List, listName='history.csv'):
    _list = []  # 返回值
    _data = pd.DataFrame(List)  # 将传入的数组变成DataFrame

    if os.path.exists("bookcase/" + listName):  # 如果文件存在，则直接保存
        test = pd.DataFrame(pd.read_csv("bookcase/" + listName, encoding='utf-8'))  # 将原文件转换成DataFrame
        # print(_data.iterrows())
        # 遍历列表
        for i in _data.iterrows():
            # 临时参数
            _i = i[1]

            if test[test['剧名'] == _i['剧名']].empty:  # 如果找不到_i的剧名，说明没有重复，可以添加到文件中
                test = test.append(_i, ignore_index=True)
            else:  # 如果剧名有重复，也可能是同一个剧到不同场次的演出，或者不同剧组的剧，所以需要判断
                _info = test[test['剧名'] == _i['剧名']]
                print()
                if _info[_info['演出场所'] == _i['演出场所']].empty or _info[
                    _info['演出时间'] == _i['演出时间']].empty:  # 如果演出时间和演出场所有一个内容是不相同的，则判断为一个戏的不同场次，所以还是要显示出来的
                    test = test.append(_i, ignore_index=True)
                else:  # 完全相同
                    print('完全重复的：', _i['剧名'])

        test.to_csv("bookcase/" + listName, header=True, index=False)

        print('更新了列表内容')
        return test
    else:  # 如果文件不存在，则直接保存并返回内容
        _data.to_csv("bookcase/" + listName, header=True, index=False)

        print('没有原始文件，列表内容全部保存')
        return _data


# 在大麦中获取内容的更详细信息
def update_list(listName='info_drama.csv', headers='https://piao.damai.cn/'):
    _list = pd.DataFrame(pd.read_csv("bookcase/" + listName, header=0, encoding='utf-8'))  # 读取CSV，以后是读取数据库

    for n, i in _list.iterrows():
        if i['信息属性'] == 0:  # 如果信息属性为0，则表示没有从大麦中获取数据，
            end = headers + str(i['projectid']) + '.html'
            get_info(end)

    # 更新列表中的内容，让他们更详细
    # 将超出时间的内容放在另一张表中，可以晚点做
    pass


def list_to_db():
    print(1)


def csv_to_db():
    print('1')


def db_to_csv():
    print('1')


def csv_to_data():
    # 读数据
    test = pd.DataFrame(pd.read_csv(curPath + '/worker/history.csv', header=0, encoding='UTF-8'))

    # 增加是否抓取详情的列
    test['蜘蛛状态'] = False
    # print(test)

    # 遍历列表
    for i in test.iterrows():
        # 临时参数
        _linshi = i[1]
        print(_linshi['蜘蛛状态'])
        # # 如果本条数据没有被爬取，则爬取
        # if i['蜘蛛状态'] == False:
        #     print('爬取数据')
        #     print('修改状态')
        break
    # #测试两个表中的数据是否相同
    # c = 0
    # for i in range(402):
    #     a = doi[i+468][2]
    #     b = yun[i][1]
    #     if a==b:
    #         c +=1
    #     # break
    # print(c)

    # #看看原来的运动表是否也是这样的数字，如果是的话，再校对一遍，然后就可以添加内容了
    # _re =[]
    # for  i in range(len(con[468:])):
    #     # print(len(con[i+468]))
    #     _de =[]
    #
    #     a = eval(con[i+468][2])
    #     b= yun[i]
    #
    #     for j in range(len(a)):
    #         a[j]['title']=b[j*3+4]
    #
    #     _de.append(str(con[i + 468][0]))
    #     _de.append(str(con[i + 468][1]))
    #     _de.append(str(a).replace(' ', ''))
    #     _de.append(str(con[i + 468][3]))
    #     _de.append(str(con[i + 468][4]))
    #
    #     _re.append(_de)
    #     # print(_de)
    #     # break

    # print(test)

    # return _re

    # 做完之后，去掉文本中的空格


# 在活动详情中，可以添加的内容包括：
# 封面地址、标题、发起人ID、参加的用户ID名单、演出时间、演出地点、演出票价、
# 照片¥视频、导演介绍&访谈、故事&编剧、演员相关、周边新闻、口碑剧评
# 演出标签、用于分析的关键词标签

if __name__ == '__main__':
    # csv_to_data()

    update_list()
    # print(curPath)
