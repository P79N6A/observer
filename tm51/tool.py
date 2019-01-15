# 公共库
import os
from bs4 import BeautifulSoup as BS
import re

# 私有库

# 将xml转成list，并返回。如果有对应文件，则直接获取
def xml_to_mini(name, key_list):
    if os.path.exists('res/%s.xml' % name):  # 存在则读取内容
        print('找到xml文件，开始读取……')

        #避免大文件导致的错误，所以逐行读取
        _file = ''
        # 打开含中文的文本
        with open('res/%s.xml' % name, 'r', encoding='utf-8') as file:
            # 按行读取
            while True:
                _i = file.readline()
                _file += _i
                # 读取完，循环结束
                if len(_i) == 0:
                    break

        # 提取row的列表
        row=re.compile(r'<row>((?:.|\n)*?)</row>')
        _row=row.findall(_file)

        # 提取数据添加到元组
        _list = []# 格式化为列表
        for i in _row:
            _i = () # 单条信息是个元组

            for _k in key_list: #b
                #提取对应字段的数据
                _key = re.compile(r'<field name="%s">(.*?)</field>'%_k)
                _i =_key.findall(i)[0]

            _list.append(_i)

        # print('转换成功：%s'%len(_list))

        # 并保存到txt
        with open('res/%s_mini.txt' % name, 'w', encoding='utf-8') as _file:
            _file.write(str(_list))

        print('创建文件：res/%s_mini.txt' % name)
        return _list
    else:
        print('没有找到xml文件……')
        exit()


# 提取数据中的指定字段，Data：list，Key_list：list
def extract_id(data, key_list):
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

    print('提取 %s 完成，一共有 %s 条内容' % (str(key_list), len(_list)))
    return _list


# 传入文件名和要提取的字段，按照字段的顺序，自动转换xml为txt，返回包含元组的列表
def get_mini(name, key_list):
    if os.path.exists('res/%s_mini.txt' % name):  # 是否存在mini版，存在则读取内容
        print('运气很好，有对应的nimi文件，开始读取……')

        with open('res/%s_mini.txt' % name, 'r', encoding='utf-8') as file:
            _list = eval(file.read())

        print('读取成功：res/%s_mini.txt' % name)
        return _list
    # elif os.path.exists('res/%s.txt' % name):  # 是否存在完整版，存在，则转换xml
    #     print('没有找到mini文件，要开始转译mini文件，需要花点时间……')
    #     # 提取xml中的内容
    #     _file = open('res/%s.txt' % name, 'r', encoding='utf-8').read()
    #
    #     _list = extract_id(_file, key_list)
    #
    #     print('读取成功：res/%s_mini.txt' % name)
    #     return _list
    else:  # 没有文件，则自己生产吧
        print('没有找到任何文件，要开始转译文件xml，稍等')
        _list=xml_to_mini(name, key_list)

        print('读取成功：res/%s_mini.txt' % name)
        return _list


# 去重
def only_one(List, No_False=None):
    print('开始进行去重操作')
    # _list = []
    # for i in List:
    #     if i not in _list:
    #         _list.append(i)
    # print('去重结束,减少了 %s 个' % (len(List) - len(_list)))
    #
    # if No_False:
    #     if 0 in _list:
    #         _list.remove(0)
    #
    #     if '' in _list:
    #         _list.remove('')
    # print('去除空置')
    #
    # return _list

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
    com_name = eval(open('res/com_name.txt', 'r', encoding='utf-8').read())

    # 排出内容人员
    _value = []
    for i in _value:
        if i not in com_name:
            _value.append(i)

    return _value


# 动作转换为文字
def change_action(list,key_list):
    # 读取动作列表
    with open('res/action_list.txt', 'r', encoding='utf-8') as action:
        _action=eval(action.read())

    key_site = key_list.index('action_type')
    for i in list:#遍历列表，在_action列表中可以找到，则变成中文，如果不在则默认不变
        if i[key_site] in _action:
            i[key_site] = _action[i[key_site]]

    print('转换完成')
    return list



if __name__ == '__main__':
    out_com()