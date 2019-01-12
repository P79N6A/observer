# 公共库
import os
from bs4 import BeautifulSoup as BS


# 私有库

# 将xml转成list，并返回。如果有对应文件，则直接获取
def xml_to_mini(name, key_list):
    if os.path.exists('res/%s.xml' % name):  # 存在则读取内容
        print('找到xml文件，开始读取……')
        _file = open('res/%s.xml' % name, 'r', encoding='utf-8').read()
        _file_clean = _file.replace('field name=', 'field class=')
        _file_bs = BS(_file_clean, 'lxml').find_all('row')

        _list = []# 格式化为列表

        # 提取数据添加到_list
        for i in _file_bs:
            _i = {}# 单条信息是个字典

            for j in i.find_all('field'):
                _name = j.get('class')[0]  # 获取单条属性的class名,class可能是数组
                if _name in key_list: #如果是需要提取的内容，则赋值
                    _i[_name] = j.text
            _list.append(_i)

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
    for i in key_list:
        if i in data[0]:  # 判断Key是否在Data中
            print('列表中包含%s' % i)
        else:
            print('列表%s中不包含%s' % (data[0], i))
            return

    # 遍历Data，采集对应内容，去重
    _list = []
    for i in data:
        _one = {}  # 单条信息
        for j in key_list:
            _one[j] = i[j]

        _list.append(_one)

    print('提取 %s 完成，一共有 %s 条内容' % (str(Key_list), len(_list)))
    return _list


# 传入文件名和要提取的字段，自动转换xml，自动生产mini版本
def get_mini(name, key_list):
    if os.path.exists('res/%s_mini.txt' % name):  # 是否存在mini版，存在则读取内容
        print('运气很好，有对应的nimi文件，开始读取……')
        _file = open('res/%s_mini.txt' % name, 'r', encoding='utf-8').read()
        _list = eval(_file)

        print('读取成功：res/%s_mini.txt' % name)
        return _list
    elif os.path.exists('res/%s.txt' % name):  # 是否存在完整版，存在，则转换xml
        print('没有找到mini文件，要开始转译mini文件，需要花点时间……')
        # 提取xml中的内容
        _file = open('res/%s.txt' % name, 'r', encoding='utf-8').read()

        _list = extract_id(_file, key_list)

        print('读取成功：res/%s_mini.txt' % name)
        return _list
    else:  # 没有文件，则自己生产吧
        print('没有找到任何文件，要开始转译文件xml，会花费大量时间……')
        _list=xml_to_mini(name, key_list)

        print('读取成功：res/%s_mini.txt' % name)
        return _list


# 去重
def only_one(List, No_False=None):
    _list = []
    for i in List:
        if i not in _list:
            _list.append(i)
    print('去重结束,减少了 %s 个' % (len(List) - len(_list)))

    if No_False:
        if 0 in _list:
            _list.remove(0)

        if '' in _list:
            _list.remove('')
    print('去除空置')

    return _list


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
def change_action(list):
    # 动作
    action_list = eval(open('res/action_list.txt', 'r', encoding='utf-8').read())

    for i in list:
        if i['action_type'] in action_list:
            i['action_type'] = action_list[i['action_type']]

    print('转换完成')
    return list


if __name__ == '__main__':
    out_com()
