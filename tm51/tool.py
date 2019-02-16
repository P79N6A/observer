# -*- coding: UTF-8 -*-
'''
公共工具
'''
# 公共库
import os
from bs4 import BeautifulSoup as BS
import re


# 私有库


# 提取数据中的指定字段，Data：list，Key_list：list
def extract_id(data,key_list):
    # for i in key_list:
    #     if i in data[0]:  # 判断Key是否在Data中
    #         print('列表中包含%s' % i)
    #     else:
    #         print('列表%s中不包含%s' % (data[0], i))
    #         return

    # 遍历Data，采集对应内容，去重
    _list = []
    for i in data:
        _one = {}  # 单条信息
        for j in key_list:
            _one[j] = i[j]

        _list.append(_one)

    print('提取 %s 完成，一共有 %s 条内容' % (str(key_list),len(_list)))
    return _list


def get_xml(name,key_list):
    """
    获取xml的对应数据，不负责保存为txt
    :param name:
    :param key_list:
    :return: 返回列表，元素为元组
    """
    print('开始：%s' % sys._getframe().f_code.co_name)
    if type(name) is list:  # 如果是列表，说明有分表，否则，就是单表
        path_xml = 'res/%s/xml/%s-%s.xml' % (name[0],name[0],name[1])
    else:
        path_xml = 'res/%s/xml/%s.xml' % (name,name)

    if os.path.exists(path_xml):  # 有文件，则读取美容
        print(r'找到文件：%s' % path_xml)

        with open(path_xml,'r',encoding='utf-8') as file:  # 打开文本
            _file = file.read()
            # print(_file)
        print(r'读取成功：%s' % path_xml)

        _row = re.findall(r'<row>((?:.|\n)*?)</row>',str(_file),re.S)  # 提取row的列表

        _list = list()  # 提取数据，创建tuple，添加到list
        for i_row in _row:  # 遍历列表，获取内容并放入元组
            _i = ()  # 单条信息是个元组
            for _k in key_list:
                # print(_k)
                _key = re.findall(r'<field name="%s">((?:.|\n)*?)</field>' % _k,i_row)  # 提取对应字段的数据
                if _key:  # 如果字段是null，则无法读取[0]，会报错，所以在没有值的时候，代入其他值
                    f_key = (_key[0],)
                else:
                    f_key = (None,)
                _i += f_key
                # print(f_key)
            _list.append(_i)

        print('转换成功：%s' % len(_list))
        return _list

    else:  # 没有文件
        print(r'没有找到文件：%s' % path_xml)
        return


def get_mini(name,key_list):
    """
    弃用，用get_xml替代
    :param name:
    :param key_list:
    :return: 返回列表，元素为元组
    """
    file_path = r'res/%s' % name
    txt_path = 'res/%s/%s.txt' % (name,name)
    xml_path = 'res/%s/%s.xml' % (name,name)

    if os.path.exists(txt_path):  # 是否存在mini版，存在则读取内容
        print('运气很好，有对应的txt文件，开始读取……')

        with open(txt_path,'rb') as file:
            _list = eval(file.read())

        print('读取成功:txt')
        return _list
    elif os.path.exists(xml_path):  # 没有txt文件，但有xml文件，则开始转化
        print('没有找到txt文件，要开始转译文件xml，稍等')

        # 打开含中文的文本
        with open(xml_path,'rb') as file:
            _file = file.read()
            # print(_file)
        print('读取成功:xml')
        # print(str(_file)[100])
        # return
        _row = re.findall(r'<row>((?:.|\n)*?)</row>',str(_file),re.S)  # 提取row的列表
        # print(_row)
        print('读取成功:xml')
        # 提取数据添加到元组
        _list = []  # 格式化为列表
        for i_row in _row:
            # print(i_row)

            # 遍历列表，获取内容并放入元组
            _i = ()  # 单条信息是个元组
            for _k in key_list:  # b
                # print(_k)

                # 提取对应字段的数据
                _key = re.findall(r'<field name="%s">((?:.|\n)*?)</field>' % _k,i_row)

                # 如果字段是null，则无法读取[0]，会报错，所以在没有值的时候，代入其他值
                if _key:
                    f_key = (_key[0],)
                else:
                    f_key = (None,)
                _i += f_key
                # print(f_key)

            _list.append(_i)

        print('转换成功：%s' % len(_list))

        new_folder(file_path)  # 如果没有文件夹，需要先创建文件夹

        # 并保存到txt
        with open(txt_path,'w',encoding='utf-8') as _file:
            _file.write(str(_list))

        print('创建文件：%s' % txt_path)
        return _list
    else:
        print('没有找到xml文件……')
        exit()


# 去重
def only_one(List):
    print('开始进行去重操作')
    return list(set(List))


# 新建文件夹
def new_folder(path):
    if not os.path.exists(path):  # 如果文件夹不存在，则新建
        os.makedirs(path)
        # print('新建文件夹%s成功' % path)
    # else:
    # print('文件夹%s已存在' % path)
    return path


# 排出内容人员的用户名
def out_com(List):
    # 自己人的账号
    com_name = eval(open('res/com_name.txt','r',encoding='utf-8').read())

    # 排出内容人员
    _value = []
    for i in _value:
        if i not in com_name:
            _value.append(i)

    return _value


# 输入英文动作，返回中文动作
def action_to_cn(aciton):
    # 读取动作列表
    with open('res/action_list.txt','r',encoding='utf-8') as action:
        action_list = eval(action.read())

    if aciton in action_list:
        aciton_cn = action_list[aciton]
        return aciton_cn
    else:
        return aciton


# 输入字典或列表，制作饼状图
def make_pie(_list,_title='无'):
    import matplotlib as mpl
    import matplotlib.pyplot as plt  # 导入画图库

    key = list()
    value = list()
    for i in _list:
        key.append(i[0])
        value.append(i[1])

    explode = [0.05,0,0,0,0,0,0,0,0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse

    mpl.rcParams['font.family'] = ['Arial Unicode MS']  # 解决中文乱码
    plt.pie(x=value,labels=key,autopct='%3.1f %%',
            shadow=False,labeldistance=1.1,startangle=90,pctdistance=0.6)

    plt.axis('equal')
    # plt.legend()
    plt.title(_title)
    plt.savefig('timeseries_y.jpg')
    plt.show()


# 输入字典或列表，制作柱状图
def make_bar(_file,_title='无'):
    import matplotlib as mpl
    import matplotlib.pyplot as plt  # 导入画图库

    _list = list(_file.items())
    _list.sort()    #排序

    x = list()
    y = list()
    for i in _list:  # 生成x、y轴数据
        x.append(r'%s月' % i[0])
        y.append(int(i[1]))

    print(x)
    plt.rcParams['font.family'] = ['Arial Unicode MS']  # 解决中文乱码

    plt.bar(x,y)  # 生成表格

    for _x,_y in zip(x,y):  # 显示刻度上的数字
        plt.text(_x,_y,_y,ha='center',va='bottom')

    plt.title(_title)  # 显示标题

    plt.savefig(r'%s.jpg' % _title)  # 保存图标
    plt.show()


# #输入列表，然后按照其中的值降序排序，前几名单独列出，其他的内容合并显示，并返回字典
def dde(dict,tops):
    _dict = list(dict.items())  # 排序后的list
    _dict.sort(key=lambda x:x[1],reverse=True)  # 降序排序

    _d = {'其他':0}  # 输出内容
    for i in range(len(_dict)):
        if i < tops:
            _d[_dict[i][0]] = _dict[i][1]
        else:
            _d['其他'] += _dict[i][1]

    print(_d)
    return _d


def fenci(txt):
    pass


# 形成3D数据
def for_3d(count_last_times):
    to_3d = []  # 制作3d坐标点
    _z = 0  # z轴值
    _last = 0  # 最后x轴值
    for i in count_last_times:  # 产出3D数据
        if _last == i[0]:
            _z += 1
        else:
            _z = 0

        to_3d.append((i[0],i[1],_z))

    print(to_3d)


if __name__ == '__main__':
    make_pie(
        [('搜索结果',25613),('社区首页',16721),('用户名片界面',16207),('首页-推文',9684),('试管婴儿版块',9217),('首页',3579),('社区-最新页签',1705)])
