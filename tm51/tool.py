# 公共库
import os
from bs4 import BeautifulSoup as BS

#私有库

# 将xml转成list，并返回。如果有对应文件，则直接获取
def get_value(Name):
    if os.path.exists('res/%s.txt' % Name):  # 存在则读取内容
        _file = open('res/%s.txt' % Name , 'r' , encoding='utf-8').read()
        _list = eval(_file)

        print('调用文件：res/%s.txt' % Name)
        return _list

    else:  # 不存在，则转换xml
        # 提取xml中的内容
        _file_1 = open('res/%s.xml' % Name , 'r' , encoding='utf-8').read()
        _file_2 = _file_1.replace('field name=' , 'field class=')
        _file_3 = BS(_file_2 , 'lxml').find_all('row')

        # 格式化为列表
        _list = [ ]

        # 提取数据添加到_list
        for i in _file_3:
            # 单条信息是个字典
            _i = {}

            for j in i.find_all('field'):
                _name = j.get('class')[ 0 ]  # 获取单条属性的class名,class可能是数组
                _i[ _name ] = j.text

            _list.append(_i)

        # 并保存到txt
        with open('res/%s.txt' % Name , 'w' , encoding='utf-8') as _file:
            _file.write(str(_list))

        print('创建文件：res/%s.txt' % Name)
        return _list


# 获取列表中的某些参数
def get_id(Data , Key_list):
    for i in Key_list:
        if Key_list in Data[ 0 ].keys():  # 判断Key是否在Data中
            print('列表%s中包含%s' % (Data , Key_list))
        else:
            print('列表%s中不包含%s' % (Data , Key_list))
            return

    # 遍历Data，采集对应内容，去重
    _list = [ ]
    for i in Data:
        _one={}#单条信息
        for j in Key_list:
            _one[j] =i[j]

        _list.append(_one)

    print('提取 %s 完成，一共有 %s 条内容' % (str(Key_list) , len(_list)))
    return _list

#去重
def only_one(List,No_False=None):
    _list=[]
    for i in List:
        if i not in _list:
            _list.append(i)
    print('去重结束,减少了 %s 个' % (len(List)-len(_list)))

    if No_False:
        _list.remove(0)
        _list.remove('')
    print('去除空置')

    return _list


# 新建文件夹
def new_flie(Name):
    path = "res/" + str(Name)

    if not os.path.exists(path):  # 如果文件夹不存在，则新建
        os.makedirs(path)
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


if __name__ == '__main__':
    out_com ()
