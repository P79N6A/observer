#回收站，把以前写的没有用的代码都放在这里

# 获取需要爬去的演出列表地址，并保存为：get_url.csv
def get_list(self):
    # 获取post数据包
    response = requests.post(url=self.url['url'], headers=self.url['headers'], data=self.url['data'])
    # print(response)

    # 将字符串数据转换成字典数据
    dict_data = json.loads(response.text)
    # print(dict_data)

    # 将需要的爬取的字典数据存储在变量中
    need_spider_data = dict_data["pageData"]["resultData"]
    # print(need_spider_data)

    # clean数据
    _clean_list = []

    # 提取内容那
    for j in range(len(need_spider_data)):
        _j = {'标题': need_spider_data[j]['name'],
              '副标题': need_spider_data[j]['subhead'],
              '地点城市': need_spider_data[j]['venuecity'],
              '演出场所': need_spider_data[j]['venue'],
              '演出时间': need_spider_data[j]['showtime'],
              '演出状态': need_spider_data[j]['showstatus'],
              '演出类型': need_spider_data[j]['subcategoryname'],
              'projectid': need_spider_data[j]['projectid'],
              'imgurl': need_spider_data[j]['imgurl'],
              '最低票价': need_spider_data[j]['price'],
              '最高票价': need_spider_data[j]['pricehigh'],
              '剧名': re.search('《[^》]+》', _j['标题'], flags=0).group()
              }

        _clean_list.append(_j)

    # 测试字典数据是否能解析出来
    print(_clean_list)

    # 保存内容到

    return _clean_list


# 获取列表中每条页面的有用信息,并保存在原来的文件中，并保存到
def get_info(self):
    _data = pd.DataFrame(
        pd.read_csv('/Users/tama1/Documents/ob/worker/readers/get_url.csv', header=0, encoding='UTF-8'))

    # # 增加是否抓取详情的列
    _data['蜘蛛状态'] = False
    # print(test)

    # 建立容器
    gat_info_list = []

    # 遍历列表
    for i in _data.iterrows():

        # 如果本条数据没有被爬取，则爬取
        if i[1]['蜘蛛状态'] == False:
            # 拼接地址
            _url = self._url_header + str(i[1]['projectid']) + '.html'
            # print(_url)

            # 打包出请求表头
            _url_info = URL_Info(_url).damai()

            # 解析页面
            # _html = pares(_url_info)
            # print(_html)

            _html = BS(_test, 'html.parser')
            dd = etree.HTML(_test)

            # 建立信息字典，单条信息是字典

            # 获取有用信息


        break
        time.sleep(5)

    # 保存到
    Save(gat_info_list, 'info_list.csv')

    return gat_info_list


# 保存为CSV数据
def save(self):
    # 构建属性列表
    # list = ['actors', 'categoryname', 'cityname', 'description', 'price', 'pricehigh', 'showstatus', 'showtime', 'subcategoryname', 'venue', 'venuecity', 'verticalPic']
    list = self.data_key

    # 此处出现保存，报错为缺少字段，因此追加一个字段
    list.append('favourable')
    # 测试list
    # print(list)

    # 数据
    my_data = self.parse()
    # 测试
    # print(my_data)

    with open("damaiwang" + ".csv", "w", newline="", encoding='utf8') as f:
        # 传入头数据，即第一行数据
        writer = csv.DictWriter(f, list)
        writer.writeheader()
        for row in my_data:
            writer.writerow(row)


# def get_list0(self, n):
#     url = "https://piao.damai.cn/" + str(n) + ".html"
#     response = requests.get(url)
#     response.encoding = "utf-8"
#     html = BS(response.text, 'html.parser')
#
#
#
#
# # # 保存为字典数据
# # def save_dict(self):
# #     with open("damaiwang", 'w', encoding='utf8') as f:
# #         f.write(str(self.parse()))
#
#
# # 返回页面的源代码,会因为反爬虫，所以需要额外做判断，之后要把这部分单独做出来
# def get_parse(info):
#     try:
#         response = requests.get(info['url'], headers=info['headers'], proxies=info['proxies'], timeout=1)
#         if response.status_code == 200:
#             # 解析内容
#             page_source = BS(response.text, 'html.parser')
#
#             # print(response.text)
#             return page_source
#         else:
#             print(response.status_code)
#             return None
#     except RequestException:
#         # 向工作日志中写入内容
#         return None


#
# # 请求url获取响应
# def post_parse(url):
#     response = requests.post(url=url['url'], headers=url['headers'], data=url['data'])
#
#     # 将字符串数据转换成字典数据
#     dict_data = json.loads(response.text)
#
#     # 将需要的爬取的字典数据存储在变量中
#     need_spider_data = dict_data["pageData"]["resultData"]
#
#     # 测试字典数据是否能解析出来
#     # print(dict_data["pageData"]["resultData"])
#     return need_spider_data



# 把传入的列表中的内容和数据库中的内容做对比，去重并返回不重复的内容
def entry_list(List, listName='history.csv'):
    _list = []  # 返回值
    _data = pd.DataFrame(List)  # 将传入的数组变成DataFrame

    if os.path.exists("res/" + listName):  # 如果文件存在，则直接保存
        test = pd.DataFrame(pd.read_csv("res/" + listName, encoding='utf-8'))  # 将原文件转换成DataFrame
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

        test.to_csv("res/" + listName, header=True, index=False)

        print('更新了列表内容')
        return test
    else:  # 如果文件不存在，则直接保存并返回内容
        _data.to_csv("res/" + listName, header=True, index=False)

        print('没有原始文件，列表内容全部保存')
        return _data





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