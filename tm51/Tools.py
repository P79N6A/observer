# coding=utf-8
# 转换内容 ，并提取数据
import os
from datetime import datetime

from requests import RequestException

from bs4 import BeautifulSoup as bs
import time

# 自己人的账号
com_name = eval(open('./res/actin_list.txt','r',encoding='utf-8').read())

#操作和名字对应表
actin_list = eval(open('./res/actin_list.txt','r',encoding='utf-8').read())


# 判断最近50个发日记的人的名单
def dd(self):
    _list = bs(self.text , 'lxml').find_all('row')

    # 排出内容人员的用户名
    _v = [ ]
    for i in com_name:
        _v.append(str(i[ 0 ]))

    # 排出内容人员
    value = [ ]
    for i in _list:
        if i.find_all('field')[ 1 ].text not in _v:
            _g = {'帖子id':i.find_all('field')[ 0 ].text , '用户ID':i.find_all('field')[ 1 ].text}
            value.append(i.find_all('field')[ 1 ].text)

    print('一共有 %d 个用户，用户ID为：%s' % (len(value) , value))

# 提取列表中的UID列表
class get_value:
    def __init__(self):
        self._forum_thread = './res/forum_thread.xml'
        self._forum_thread_txt = './res/forum_thread.txt'

        self._user_action_report = './res/user_action_report.xml'
        self._user_action_report_txt = './res/user_action_report.txt'

        self._user_count = './res/user_count.xml'
        self._user_count_txt = './res/user_count.txt'

    def _get_value(self , Path):
        # 将内容格式化
        _text = open(Path , 'r' , encoding='utf-8').read()
        _switch = _text.replace('field name=' , 'field class=')
        _list = bs(_switch , 'lxml').find_all('row')

        # 格式化为列表
        _re = [ ]
        for i in _list:
            _j = {}
            for j in i.find_all('field'):
                _j[ j.get('class')[ 0 ] ] = j.text

            _re.append(_j)
            # print(_re)
        return _re

    @property  # 提取'../res/forum_thread.xml'中的内容
    def forum_thread(self):
        isExists = os.path.exists(self._forum_thread_txt)

        if isExists:  # 存在则读取内容
            _file = open(self._forum_thread_txt , 'r' , encoding='utf-8').read()
            _value = eval(str(_file))
            print('调用文件：_forum_thread_txt')

        else:  # 不存在，则转换xml
            _value = self._get_value(self._forum_thread)

            # 并保存到txt
            _file = open(self._forum_thread_txt , 'w' , encoding='utf-8')
            _file.write(str(_value))
            _file.close()
            print('创建文件：_forum_thread_txt')

        return _value

    @property
    def user_action_report(self):
        isExists = os.path.exists(self._user_action_report_txt)

        if isExists:  # 存在则读取内容
            _file = open(self._user_action_report_txt , 'r' , encoding='utf-8').read()
            _value = eval(str(_file))
            print('调用文件：_user_action_report_txt')

        else:  # 不存在，则转换xml
            _value = self._get_value(self._user_action_report)

            # 并保存到txt
            _file = open(self._user_action_report_txt , 'w' , encoding='utf-8')
            _file.write(str(_value))
            _file.close()
            print('创建文件：_user_action_report_txt')

        return _value

    @property  # 提取'../res/forum_thread.xml'中的内容
    def user_count(self):
        isExists = os.path.exists(self._user_count_txt)

        if isExists:  # 存在则读取内容
            _file = open(self._user_count_txt , 'r' , encoding='utf-8').read()
            _value = eval(str(_file))
            print('调用文件：user_action_report.txt')

        else:  # 不存在，则转换xml
            _value = self._get_value(self._user_count)

            # 并保存到txt
            _file = open(self._user_count_txt , 'w' , encoding='utf-8')
            _file.write(str(_value))
            _file.close()
            print('创建文件：user_action_report.txt')

        return _value
# 工具组件
class Tool:
    # 获取列表中的uid
    def get_uid(self , Data,Key):  # 提取用户ID、并去除0
        if Key in Data[0].keys():
            print('列表中包含%s'%Key)
            _value = [ ]
            for i in Data:
                if i[ Key ] not in _value:
                    # print(type(i[ 'uid' ]))
                    _value.append(i[ Key ])

            if '0' in _value:
                _value.remove('0')

            return _value
        else:
            print('列表中不包含%s' % Key)

            return

    # 新建文件夹
    def new_flie(self , Name):
        path = "./res/" + str(Name)
        # 判断路径是否存在
        isExists = os.path.exists(path)

        # print(isExists)
        # 判断结果
        if not isExists:
            os.makedirs(path)

        return path

    def out_com(self , List):
        # 排出内容人员的用户名
        _v = [ ]
        for i in com_name:
            _v.append(str(i[ 0 ]))

        # 排出内容人员
        value = [ ]
        for i in List:
            if i not in _v:
                value.append(i)

        return value


# 查看没有发帖的用户在做什么，保存到了res文件夹
def action():
    # 创建文件夹
    file_50 = Tool().new_flie(50)
    file_100 = Tool().new_flie(100)
    file_1000 = Tool().new_flie(1000)

    _v_forum_thread = get_value().forum_thread  # 今天发帖的记录
    _uid_forum_thread = Tool().get_uid(_v_forum_thread)  # 今天发帖用户的ID列表
    print('发帖人数：%d' % len(_uid_forum_thread))

    _uid_forum_thread = Tool().out_com(_uid_forum_thread)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_forum_thread))

    # 今天操作用户的ID列表
    _v_user_action_report = get_value().user_action_report  # 今天操作记录
    _uid_user_action_report = Tool().get_uid(_v_user_action_report)  # 今天操作的用户列表
    print('活跃人数：%d' % len(_uid_user_action_report))

    _uid_user_action_report = Tool().out_com(_uid_user_action_report)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_user_action_report))

    # 将今日发帖的用户从操作的用户中去除
    _out_list = [ ]
    for i in _uid_user_action_report:
        if i not in _uid_forum_thread:
            _out_list.append(i)

    # 提取用户在操作中的记录
    for _uid in _out_list:  # 逐个处理列表中的数据
        # 用于保存一个用户到所有操作
        _list = [ ]

        # 从操作列表中提取对用用户ID的行动
        for j in _v_user_action_report:

            if _uid == j[ 'uid' ]:  # 如果在操作记录中找到这个人到ID
                # 用于保存一条操作：时间和操作
                _v = [ ]

                # 时间
                _v.append(datetime.strptime(j[ 'created_at' ] , "%Y-%m-%d %H:%M:%S").time())

                # 动作
                if j[ 'action_type' ] in actin_list:
                    _v.append(actin_list[ j[ 'action_type' ] ])

                # 去重
                if _v not in _list:
                    _list.append(_v)

        # 根据用户操作到次数，分文件夹保存数据
        if len(_list) <= 50:
            # 创建文件
            _save = open('%s/%s.txt' % (file_50,_uid) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        elif len(_list) > 50 and len(_list) <= 100:
            # 创建文件
            _save = open('%s/%s.txt' % (file_100,i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        else:
            # 创建文件
            _save = open('%s/%s.txt' % (file_1000,i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()

        # 在这里做一个统计，用户进行了多少次操作
        print(str(_uid) + ',' + str(len(_list)) + '\n')
        # break

    print('50条操作的用户有：' + str(len(os.listdir(file_50))))
    print('100条操作的用户有：' + str(len(os.listdir(file_100))))
    print('50条操作的用户有：' + str(len(os.listdir(file_1000))))


# 传入文件名，得出用户的记录条数
def numbers(Path):
    file_path = './res/' + str(Path)  # 文件路径
    file_name = './res/file_' + str(Path)  # 文件名

    _file_list = os.listdir(file_path)  # 文件名列表

    # 所有操作进行计数
    _file_time = {}
    for i in _file_list:
        _file = open(file_path + '/' + i , 'r' , encoding='utf-8')
        _list = _file.readlines()

        for j in _list:
            _d = j.split(" ")
            if _d[ 1 ] not in _file_time:
                _file_time[ _d[ 1 ] ] = 1
            else:
                _file_time[ _d[ 1 ] ] += 1

        _file.close()

    # 打印数据
    _end = open(file_name + '.txt' , 'w' , encoding='utf-8')

    # 操作记录的总条数
    _times = 0

    _list_50 = [ ]
    for i in _file_time:
        # 计算总数
        _times += _file_time[ i ]

        # 写入到文件中
        _end.write(str(i) + ',' + str(_file_time[ i ]))
        _end.write('\r\n')

    _end.write('一共有：%s 个用户记录，总共有 %s 条操作记录' % (len(_file_list) , _times))

    _end.close()

#获取童梦币前dd名
def top():
    _v_user_count = get_value().user_count
    dd= Tool().get_uid(_v_user_count,'coin')
    print(dd)

if __name__ == '__main__':
    # action()
    # numbers(50)
    # numbers(100)
    # numbers(1000)
    top()