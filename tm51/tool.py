# 公共库
import os
from bs4 import BeautifulSoup as BS
import re


# 私有库


# 提取数据中的指定字段，Data：list，Key_list：list
def extract_id(data , key_list):
    # for i in key_list:
    #     if i in data[0]:  # 判断Key是否在Data中
    #         print('列表中包含%s' % i)
    #     else:
    #         print('列表%s中不包含%s' % (data[0], i))
    #         return

    # 遍历Data，采集对应内容，去重
    _list = [ ]
    for i in data:
        _one = {}  # 单条信息
        for j in key_list:
            _one[ j ] = i[ j ]

        _list.append(_one)

    print('提取 %s 完成，一共有 %s 条内容' % (str(key_list) , len(_list)))
    return _list


def get_mini(name , key_list):
    """
    对应文件数据，如果没有则自动转换，返回列表，包含元组
    :param name:
    :param key_list:
    :return: 返回列表，元素为元组
    """
    file_path = 'res/%s' % name
    txt_path = 'res/%s/%s.txt' % (name , name)
    xml_path = 'res/%s.xml' % name

    if os.path.exists(txt_path):  # 是否存在mini版，存在则读取内容
        print('运气很好，有对应的txt文件，开始读取……')

        with open(txt_path , 'r' , encoding='utf-8') as file:
            _list = eval(file.read())

        print('读取成功：%s' % txt_path)
        return _list
    elif os.path.exists(xml_path):  # 没有txt文件，但有xml文件，则开始转化
        print('没有找到txt文件，要开始转译文件xml，稍等')

        # 打开含中文的文本
        with open(xml_path , 'r' , encoding='utf-8') as file:
            _file = file.read()
            # print(_file)

        _row = re.findall(r'<row>((?:.|\n)*?)</row>' , _file , re.S)  # 提取row的列表
        # print(_row)

        # 提取数据添加到元组
        _list = [ ]  # 格式化为列表
        for i_row in _row:
            # print(i_row)

            # 遍历列表，获取内容并放入元组
            _i = ()  # 单条信息是个元组
            for _k in key_list:  # b
                # print(_k)

                # 提取对应字段的数据
                _key = re.findall(r'<field name="%s">(.*?)</field>' % _k , i_row)

                # 如果字段是null，则无法读取[0]，会报错，所以在没有值的时候，代入其他值
                if _key:
                    f_key = (_key[ 0 ] ,)
                else:
                    f_key = (None ,)
                _i += f_key
                # print(f_key)

            _list.append(_i)

        print('转换成功：%s' % len(_list))

        new_folder(file_path)  # 如果没有文件夹，需要先创建文件夹

        # 并保存到txt
        with open(txt_path , 'w' , encoding='utf-8') as _file:
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
    com_name = eval(open('res/com_name.txt' , 'r' , encoding='utf-8').read())

    # 排出内容人员
    _value = [ ]
    for i in _value:
        if i not in com_name:
            _value.append(i)

    return _value


# 输入英文动作，返回中文动作
def action_to_cn(aciton):
    # 读取动作列表
    with open('res/action_list.txt' , 'r' , encoding='utf-8') as action:
        action_list = eval(action.read())

    if aciton in action_list:
        aciton_cn = action_list[ aciton ]
        return aciton_cn
    else:
        return aciton


if __name__ == '__main__':
    change_action()
