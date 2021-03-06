# coding=utf-8
"""
关于用户行为统计的各种工具
"""

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime  # 日期处理
import re
import numpy as np  # 计算

# 私有库
from tm51.tool import get_xml,new_folder,action_to_cn,make_pie,dde

"""
# CREATE TABLE `user_action_report` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `from_client` int(11) NOT NULL,
#   `client_version` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '0' COMMENT '手机系统版本',
#   `app_version` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '0' COMMENT 'app版本',
#   `action_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '用户行为',
#   `uid` int(11) NOT NULL COMMENT '用户id',
#   `device_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '设备id',
#   `info` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '行为的附加信息',
#   `remote_ip` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT 'ip地址',
#   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
#   PRIMARY KEY (`id`)
# ) ENGINE=MyISAM AUTO_INCREMENT=4428820 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户行为表';
"""

class_list = [20,50,100,150]  # 根据操作次数分文件夹保存
tops_num = 8  # 设置显示前几名的内容
_split_ = '\t'  # 统计报告的分隔符号
name = 'user_action_report'
path = new_folder('res/%s' % name)
path_device_file = new_folder('%s/%s' % (path,'device'))  # 新建文件夹

list_key = ['id','from_client','client_version','app_version','action_type','uid','device_id','info','remote_ip',
            'created_at']
site_id = list_key.index('id')  # id位置
site_from_client = list_key.index('from_client')  # from_client位置
site_client_version = list_key.index('client_version')  # client_version位置
site_app_version = list_key.index('app_version')  # app_version位置
site_action_type = list_key.index('action_type')  # action_type位置
site_uid = list_key.index('uid')  # uid位置
site_device_id = list_key.index('device_id')  # device_id位置
site_info = list_key.index('info')  # info位置
site_remote_ip = list_key.index('remote_ip')  # remote_ip位置
site_created_at = list_key.index('created_at')  # created_at位置

"""生成txt数据，生成单个用户的文件"""


def get_txt(name_date):
    """
    传入name_date为:2019_02
    从user_action_report文件夹中的txt文件夹中查找对应文件
    如果没有txt文件，则从xml文件夹中查找对应xml文件，生成txt文件。则返回此文件的内容
    如果有文件，则返回此文件的内容
    :return: 返回整个数据表，单个元素('8029', '27', 'sitePersonalCenter', '6034917', 'ffffffff-cdee-8173-ffff-ffff95527399', '2018-09-29 10:28:56')
    """
    print(__name__)
    path_txt = r'%s/txt/%s-%s.txt' % (path,name,name_date)
    # print(path_txt)
    if os.path.exists(path_txt):  # 如果有文件，则读取文件，并返回
        with open(path_txt,'r') as file:
            _file = eval(file.read())

        print(r'找到文件：%s' % path_txt)
        # print(r'找到文件：%s' % _file)
        return _file  # 转换数据，获取想要的字段
    else:  # 如果没有文件，则读取xml，保存txt，并返回
        _file = get_xml([name,name_date],list_key)

        with open(path_txt,'w') as file:  # 保存内容
            file.write(str(_file))

        print(r'找到文件：%s' % path_txt)
        # print(r'找到文件：%s' % _file)
        return _file  # 转换数据，获取想要的字段


def mak_uid_file(data):
    """
    传入数据，用来更新uid文件夹中的文件，重复的内容不会被添加进去
    :rtype: object
    """
    list_uid_times = list()  # 获取非游客用户的UID和操作日期,元素：[('6056857', '2018-09-30')]
    for i in data:
        if i[site_uid] != '0':  # 搜集非游客用户的数据
            _uid = str(i[site_uid])  # 获取用户ID
            _date = str(datetime.strptime(i[site_created_at],"%Y-%m-%d %H:%M:%S").date())  # 获取操作日期

            _i = (_uid,_date)
            list_uid_times.append(_i)  # 添加记录
    list_uid_times = list(set(list_uid_times))  # 去重，使得每个ID一天只有一条记录
    print('本月注册用户登录天/次：%s' % len(list_uid_times))

    list_uid = list()  # 本月登录的uid列表，元素：['6056842']
    for i in list_uid_times:
        list_uid.append(i[0])
    list_uid = list(set(list_uid))  # 去重，uid清单
    print('本月活跃的注册用户:%s' % len(list_uid))
    # print('本月活跃的注册用户:%s' % list_uid)

    list_file = {}  # 获取uid文件夹内列表,元素：{'6058256': '01-6058256-苹果'}
    path_file = new_folder('res/%s/%s' % (name,'uid'))  # 新建文件夹
    for i in os.listdir(path_file):
        if '.' not in i:  # 排除系统文件
            _i = i.split(r'-')
            list_file[_i[1]] = i
    # print(r'文件列表：%s' % list_file)

    _plan = 0  # 统计更新进度

    for _k in list_uid:  # 遍历list_uid，获取每个uid的行动，并保存在txt文件中
        data_uid_new = list()  # 获取uid对应的数据，元素：id、时间、操作
        _client = ''  # 判断用户的手机类型
        for i in data:
            if i[site_uid] == _k:
                _id = i[site_id]
                _action_type = action_to_cn(i[site_action_type])
                _created_at = i[site_created_at]
                data_uid_new.append((int(_id),_created_at,_action_type))  # 获取元组

                if i[site_client_version].isdigit():  # 判断用户的手机类型
                    _client = '安卓'
                else:
                    _client = '苹果'
        # print(r'手机型号：%s'%_client)

        data_uid_old = []  # 如果有旧文件，则提取内容，并删除文件
        if _k in list_file:
            _path = r'%s/%s' % (path_file,list_file[_k])
            with open(_path,'r') as file:  # 提取文件内容
                _file = file.read().strip('\n').split(u'\n')
                # print(r'_file:%s' % _file)
                for i_file in _file:
                    _i_file = i_file.split(u'\t')
                    data_uid_old.append((int(_i_file[0]),_i_file[1],_i_file[2]))
            # print(r'有原文件:%s' % data_uid_old)
            os.remove(_path)  # 删除文件
        _v_data_uid_old = len(data_uid_old)  # 旧文件内容的动作条数，用于对比新文件是否有变化

        data_uid = data_uid_old + data_uid_new
        data_uid = list(set(data_uid))  # 去重
        _v_data_uid = len(data_uid)  # 新文件内容的动作条数，用于对比新文件是否有变化
        data_uid.sort()  # 排序

        login_times = []  # 获取用户的登录日期，用于命名文件
        for i in data_uid:
            _i = str(datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").date())
            login_times.append(_i)
            login_times = list(set(login_times))  # 去重,只剩下登录日期

        with open('%s/%03d-%s-%s' % (path_file,len(login_times),_k,_client),'w',encoding='utf-8') as file:  # 保存文件
            for i in data_uid:  # 遍历数据表，符合条件，则添加到_one_list
                file.write(u'%s\t%s\t%s\r' % (i[0],i[1],i[2]))  # 写入数据

        if _v_data_uid > _v_data_uid_old:  # 如果新增
            _v = '有新增'
        elif _v_data_uid == _v_data_uid_old:  # 如果相等
            _v = '无新增'
        else:
            _v = '异常'

        _plan += 1
        print(r'更新进度 (%s/%s): %03d-%s-%s %s' % (_plan,len(list_uid),len(login_times),_k,_client,_v))

    path_report = r'res/user_action_report/月份用户报告.txt'  # 生成月份报告
    if not os.path.exists(path_report):  # 如果没有文件，创建文件，增加表头
        with open(path_report,'w') as file:
            file.write('年月\t活跃用户数\t登录天/次')
    with open(path_report,'a+') as file:
        _file = '\r%s\t%s\t%s' % (list_uid_times[0][1][:7],len(list_uid),len(list_uid_times))
        file.write(_file)


def make_device_file(data):
    """
    按照设备来统计，可以获得游客状态的用户到底在做什么
    :rtype: object
    """
    list_device_times = list()  # 获取非游客用户的设备号和操作日期,元素：[('ffffffff-8ee2-37bb-ffff-ffff81ff137f', '2018-09-29')
    for i in data:
        _device = str(i[site_device_id])  # 获取设备号
        _date = str(datetime.strptime(i[site_created_at],"%Y-%m-%d %H:%M:%S").date())  # 获取操作日期

        _i = (_device,_date)
        list_device_times.append(_i)  # 添加记录
    list_device_times = list(set(list_device_times))  # 去重，使得每个设备号一天只有一条记录
    print('本月设备登录天/次：%s' % len(list_device_times))
    # print('本月设备登录天/次：%s' % list_device_times)

    list_device = list()  # 本月登录的device列表，元素：['6056842']
    for i in list_device_times:
        list_device.append(i[0])
    list_device = list(set(list_device))  # 去重，device清单
    print('本月设备数:%s' % len(list_device))
    # print('本月活跃的注册用户:%s' % list_uid)

    list_file = {}  # 获取uid文件夹内列表,元素：{'46C74AFE': '001-46C74AFE-95C1-4BB3-973A-DFE0F7223209'
    path_file = new_folder('res/%s/%s' % (name,'device'))  # 新建文件夹
    for i in os.listdir(path_file):
        if '.' not in i:  # 排除系统文件
            _i = i.split(r'_')
            list_file[_i[1]] = i
    # print(r'文件列表：%s' % list_file)

    _plan = 0  # 统计更新进度
    for _k in list_device:  # 遍历list_uid，获取每个uid的行动，并保存在txt文件中
        data_device_new = list()  # 获取device对应的数据，元素：[(9361, '2018-09-29 18:33:20', '0', '启动APP')]
        for i in data:
            if i[site_device_id] == _k:
                _id = i[site_id]
                _created_at = i[site_created_at]
                _uid = i[site_uid]
                _action_type = action_to_cn(i[site_action_type])
                data_device_new.append((int(_id),_created_at,_uid,_action_type))  # 获取元组
        # print(r'新文件：%s'%data_device_new)

        data_device_old = []  # 如果有旧文件，则提取内容，并删除文件
        if _k in list_file:
            _path = r'%s/%s' % (path_file,list_file[_k])
            with open(_path,'r') as file:  # 提取文件内容
                _file = file.read().strip('\n').split(u'\n')
                # print(r'_file:%s' % _file)
                for i_file in _file:
                    _i_file = i_file.split(u'\t')
                    data_device_old.append((int(_i_file[0]),_i_file[1],_i_file[2],_i_file[3]))
            # print(r'原文件:%s' % data_device_old)
            os.remove(_path)  # 删除文件
        _v_data_device_old = len(data_device_old)  # 旧文件内容的动作条数，用于对比新文件是否有变化

        data_device = data_device_old + data_device_new
        data_device = list(set(data_device))  # 去重
        _v_data_device = len(data_device)  # 新文件内容的动作条数，用于对比新文件是否有变化
        data_device.sort()  # 排序
        # print(r'组合文件:%s' % data_device)

        login_times = []  # 获取device的登录日期，用于命名文件
        for i in data_device:
            _i = str(datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").date())
            login_times.append(_i)
            login_times = list(set(login_times))  # 去重,只剩下登录日期

        with open('%s/%03d_%s' % (path_file,len(login_times),_k),'w',encoding='utf-8') as file:  # 保存文件
            for i in data_device:  # 遍历数据表，符合条件，则添加到_one_list
                file.write(u'%s\t%s\t%s\t%s\r' % (i[0],i[1],i[2],i[3]))  # 写入数据

        if _v_data_device > _v_data_device_old:  # 如果新增
            _v = '有新增'
        elif _v_data_device == _v_data_device_old:  # 如果相等
            _v = '无新增'
        else:
            _v = '异常'

        _plan += 1
        print(r'更新进度 (%s/%s): %03d_%s %s' % (_plan,len(list_device),len(login_times),_k,_v))

    path_report = r'res/user_action_report/月份设备报告.txt'  # 生成月份报告
    if not os.path.exists(path_report):  # 如果没有文件，创建文件，增加表头
        with open(path_report,'w') as file:
            file.write('年月\t设备数\t登录天/次')
    with open(path_report,'a+') as file:
        _file = '\r%s\t%s\t%s' % (list_device_times[0][1][:7],len(list_device),len(list_device_times))
        file.write(_file)


"""获取搜索列表"""


# 获取所有设备列表，元素：['001_6F76FB62-3C7D-4060-92E9-68CCDC427786']
def _get_list_all_device():
    list_file = list()
    for i in os.listdir(path_device_file):
        if '.' not in i:  # 排除系统文件
            list_file.append(i)
    print('获取文件列表：%s' % len(list_file))
    # print(list_file)
    return list_file


# 在device文件夹中查找只是游客的用户，并生成文件visitor.txt,默认不重新生成新文件
def _get_list_visitor(_reset=False):
    print(r'开始查找游客用户')
    path_file = '%s/%s' % (path,'visitor.txt')  # 文件地址

    if not os.path.exists(path_file) or _reset:
        print('生成文件：%s' % path_file)
        list_visitor = list()  # 返回值

        _plan = 0  # 统计更新进度

        list_file = _get_list_all_device()  # device文件夹中的文件列表
        for i_path_file in list_file:  # 查找只包含uid为0的用
            _i_path_file = r'%s/%s' % (path_device_file,i_path_file)
            with open(_i_path_file,'r') as file:  # 打开用户操作的文件
                _file = file.readlines()

            _visitor = True
            for i in _file:
                txt = i.strip('\n').split("\t")[2]  # 提取uid
                if int(txt) != 0:
                    _visitor = False
                    break

            if _visitor:  # 添加游客到列表
                list_visitor.append(i_path_file)

            _plan += 1
            print(r'更新进度 (%s/%s)' % (_plan,len(list_file)))

        print(u'游客总数：%s\r游客占总设备的比例：%0.2f' % (len(list_visitor),len(list_visitor) / len(list_file)))

        with open(path_file,'w') as file:
            file.write(str(list_visitor))
        print('生成文件：%s(%s)' % (path_file,len(list_visitor)))
    else:
        with open(path_file,'r') as file:
            list_visitor = eval(file.read())
        print('找到文件：%s(%s)' % (path_file,len(list_visitor)))

    return list_visitor


# 在device文件夹中只登录过一天的设备，并生成文件 day_n.txt ,默认不重新生成新文件
def _get_list_few_day(_number=1,_reset=False):
    print(r'开始查找只登录一次的设备')
    path_file = '%s/day_%s.txt' % (path,str(_number))  # 文件地址

    if not os.path.exists(path_file) or _reset:
        print('生成文件：%s' % path_file)
        list_few_day = list()  # 返回值

        _plan = 0  # 统计更新进度

        list_file = _get_list_all_device()  # device文件夹中的文件列表
        for _path in list_file:
            if int(_path.split('_')[0]) == _number:  # 筛选只登录了一天的设备
                list_few_day.append(_path)

            _plan += 1
            print(r'更新进度 (%s/%s)' % (_plan,len(list_file)))

        print(u'登录%s天的用户总数：%s\r占总设备的比例：%0.2f' % (str(_number),len(list_few_day),len(list_few_day) / len(list_file)))

        with open(path_file,'w') as file:
            file.write(str(list_few_day))
        print('生成文件：%s(%s)' % (path_file,len(list_few_day)))
    else:
        with open(path_file,'r') as file:
            list_few_day = eval(file.read())
        print('找到文件：%s(%s)' % (path_file,len(list_few_day)))

    return list_few_day


"""统计"""


# 传入列表，统计每个操作的次数/统计帖子详情前页面的次数
class show_view_time:
    def __init__(self,list_file):
        self.list_file = list_file  # 要统计的列表

        self.x_list = ['首页','首页-推文','社区首页','消息页面','个人中心-帖子','用户名片界面','试管婴儿版块','喜报版块','搜索结果','童梦母婴版块','社区-全部版块',
                       '社区-精华页签',
                       '社区-最新页签','社区-热门版块']  # 统计的界面

        self.count_all_action = {}  # 统计所有设备的界面数据
        self.count_every_action = list()  # 统计每一个设备的界面数据
        self.count_last_action = {}  # 统计所有设备的上一个界面数据

    def main(self):
        _plan = 0  # 进度统计
        for _path in self.list_file:
            with open('%s/%s' % (path_device_file,_path),'r') as file:  # 统计进入帖子详情时，用户是在什么界面
                _file = file.readlines()
            # print(_file)

            list_all = {}  # 统计单个设备的所有界面次数
            list_last = {}  # 统计单个设备的上一个界面次数

            the_last = ''  # 记录上一步
            for i in _file:
                txt = i.strip('\n').split("\t")[3]  # 提取界面
                if txt in self.x_list:  # 统计上一步界面的次数
                    the_last = txt
                elif txt == '帖子详情':
                    list_last[the_last] = list_last.get(the_last,0) + 1

                list_all[txt] = list_all.get(txt,0) + 1  # 统计所有界面的次数

            for key,value in list_all.items():  # 统计总界面
                self.count_all_action[key] = self.count_all_action.get(key,0) + value

            for key,value in list_last.items():  # 统计总上一个界面
                self.count_last_action[key] = self.count_last_action.get(key,0) + value

            self.count_every_action.append(list_all)

            _plan += 1
            print(r'更新进度 (%s/%s):%s     %s' % (_plan,len(self.list_file),_path,len(_file)))

        total_list_all_file = 0  # 总计
        for i in self.count_all_action.values():
            total_list_all_file += i

        total_list_all_file_last = 0  # 总计
        for i in self.count_last_action.values():
            total_list_all_file_last += i

        self.count_all_action = list(set(self.count_all_action.items()))  # 排序所有设备的界面数据
        self.count_all_action.sort(key=lambda x:x[1],reverse=True)

        self.count_last_action = list(set(self.count_last_action.items()))  # 排序所有设备的上一个界面数据
        self.count_last_action.sort(key=lambda x:x[1],reverse=True)

        # print(list_all_file)
        # print(list_all_file_last)

    # 返回每个设备的所有操作的计数
    @property
    def list_every_action(self):
        """
        返回一个列表，列表中的每个元素都是一个用户的所有操作的计数
        {'社区首页': 6, '启动APP': 6, '消息页面': 6, '弹出框提示': 5, '首页': 5}
        不能作为饼状图
        """
        self.main()
        print('返回每个设备所有操作的统计:%s' % self.count_every_action)
        return self.count_every_action

    # 返回所有设备所有操作的计数
    @property
    def all_action(self):
        """
        返回一个列表，列表中的每个元素都是一个操作的计数
        ('请求数据时', 175012)
        可以作为饼状图
        """
        self.main()
        print('返回所有设备所有操作的统计:%s' % self.count_all_action)
        return self.count_all_action

    # 返回所有设备在帖子详情前操作的统计
    @property
    def last_action(self):
        """
        返回一个列表，列表中的每个元素都是一个操作的计数
        ('请求数据时', 175012)
        可以作为饼状图
        """
        self.main()
        print('返回所有设备在帖子详情前操作的统计:%s' % self.count_last_action)
        return self.count_last_action


# 根据传入数据的操作次数，统计某个操作的使用比例
def count_one_percent(action,list_file):
    """
    :param action: 传入需要统计的操作（中文）
    :param list_file: 传入需要统计的数据列表（可以是设备也可以是UID）
    :return: 列表，单个元素为（总操作次数，指定动作的操作次数）
    """
    print(r'开始统计%s的使用占比' % action)
    count_last_times = [[],[]]  # 统计所有的次数，元素(操作次数,此行动的操作次数)

    _plan = 0  # 进度统计

    for _path in list_file:
        with open('%s/%s' % (path_device_file,_path),'r') as file:  # 统计进入帖子详情时，用户是在什么界面
            _file = file.readlines()

        file_count = 0  # 有效去的次数统计
        time_count = 0  # 指定操作的次数统计
        for i in _file:
            _list = i.strip('\n').split("\t")  # 提取界面
            _action = _list[-1]  # 操作内容
            _time = datetime.strptime(_list[1],"%Y-%m-%d %H:%M:%S").date()  # 时间

            if _time >= datetime.strptime('2019-01-30',"%Y-%m-%d").date():
                file_count += 1

                if _action == action:
                    time_count += 1
                    count_last_times[1].append(i)

        count_last_times[0].append((file_count,time_count))
        count_last_times[0].sort(key=lambda x:x[1])

        _plan += 1
        print(r'更新进度 (%s/%s):%s     %s' % (_plan,len(list_file),_path,len(_file)))

    print(count_last_times)

    _sum = 0
    _one = 0
    for i in count_last_times[0]:
        _sum += i[0]
        _one += i[1]

    print('操作次数:%s,总操作次数:%s,占比:%0.2f' % (_one,_sum,_one / _sum))
    return count_last_times


"""小工具"""


# 查找uid所使用的设备号，返回包含此uid的设备列表
def find_device(uid):
    print('查找设备号')
    list_device = list()

    list_file = _get_list_all_device()  # 调用
    _plan = 0  # 统计更新进度
    for path_file in list_file:
        # print(path_file)
        with open('%s/%s' % (path_device_file,path_file),'r') as file:  # 统计进入帖子详情时，用户是在什么界面
            _file = file.readlines()

        for i in _file:
            txt = i.strip('\n').split("\t")[2]  # 提取uid
            if int(txt) == uid:
                list_device.append(path_file)
                break

        _plan += 1
        print(r'更新进度 (%s/%s)' % (_plan,len(list_file)))

    print(list_device)
    return list_device


# 查看单个设备的情况
def see_device(list_file):
    print('开始查找设备')
    if type(list_file) is str:
        _path = list_file.split('_')[1]
        with open(r'%s/%s' % (path_device_file,list_file),'r') as file:
            _file = file.read()
        print(_file)
    else:
        for _path in list_file:
            print('开始查找设备:%s' % _path)
            with open(r'%s/%s' % (path_device_file,_path),'r') as file:
                _file = file.read()
            print(_file)
            print('\r\r\r')


# 统计用户在首页 点击功能按钮的次数
def show_home_times():
    with open('%s/xml/user_action_report-clickHomeTopic.xml' % path,'r') as file:
        _file = file.read()

    aa = re.findall('{&amp;quot;title&amp;quot;:((?:.|\n)*?)&',_file,flags=0)  # 提取需要的中文

    txt = {}  # 统计数量
    for i in aa:
        txt[i] = txt.get(i,0) + 1

    list(set(txt.items()))
    print(txt)

    make_pie(list(set(txt.items())))


"""待整理"""


# 针对消息按钮，统计消息按钮是游客用户的第几次点击操作
def count_site_news(_txt,list_file):
    """
    :param _txt: 需要查询的动作
    :param list_file:需要查询的设备列表
    :return: 显示此动作在列表中，是第几个位置出现的
    """
    print('开始统计%s在操作中的位置' % _txt)
    count_list = list()  # 统计数据

    _plan = 0  # 进度统计
    for _path in list_file:
        with open('%s/%s' % (path_device_file,_path),'r') as file:  # 统计进入帖子详情时，用户是在什么界面
            _file = file.readlines()

        _v = 0  # 统计序号
        for i in _file:
            txt = i.strip('\n').split("\t")[-1]  # 提取uid
            _v += 1

            if txt == _txt:
                count_list.append(_v)
                break  # 找到第一个以后就停止

        _plan += 1
        print(r'更新进度 (%s/%s)' % (_plan,len(list_file)))

    print(count_list)
    # 均值
    _mean = np.mean(count_list)
    # 中位数
    _median = np.median(count_list)

    print('平均数：%s\t中位数：%s' % (_mean,_median))


# 统计不同操作数区间的用户，他们各种操作占有的比例
def create_report():
    total_dict = {}  # 数据报告列表
    txt_dict = {}  # 迷你报告内容

    # 扫描文件夹，提取其中的文件夹
    file_list = os.listdir(path)  # 获取文件夹的所有文件和目录
    for i in file_list:
        if os.path.isdir('%s/%s' % (path,i)):  # 如果是一个文件夹，则扫描
            txt_dict[i] = {}  # 建立一个元素
            # print(file_path)

            file_list = os.listdir('%s/%s' % (path,i))  # 获取文件名列表
            print('%s文件夹数量：%s' % (i,len(file_list)))

            file_times = {}  # 所有操作进行计数
            times_total = 0  # 总操作次数

            # 统计文件夹中所有文件中的操作数量
            for i_file_list in file_list:  # 遍历文件表
                with open('%s/%s' % ('%s/%s' % (path,i),i_file_list),'r',encoding='utf-8') as _file:
                    _list = _file.readlines()

                    for i_list in _list:
                        _i_list = i_list.replace('\n','').split("\t")
                        # print(_i_list)
                        # 如果在字典中，就+1，不在则=1
                        if _i_list[1] not in file_times:
                            file_times[_i_list[1]] = 1
                            times_total += 1
                        else:
                            file_times[_i_list[1]] += 1
                            times_total += 1
                    # break
            print('总操作次数:%s\n' % times_total)

            # 将统计内容添加到数组
            txt_dict[i]['统计独立设备数'] = len(file_list)
            txt_dict[i]['总操作次数'] = times_total
            txt_dict[i]['人平均操作次数'] = times_total / len(file_list)

            # 将内容汇总到一个字典中
            total_dict[i] = file_times

        else:
            print('%s不是文件夹\n' % i)

    # 填充表头，保证每个不同的表中包含的所有表头都添加进去
    total_list = []
    for i in total_dict.values():
        for _i in i:
            if _i not in total_list:
                total_list.append(_i)

    # 直接在表中原表中加入汇总，这样就不用单独用一个数了
    total_total_dict = {}
    # 向汇总表中填充空列表，用于占位置
    for i in total_list:
        total_total_dict[i] = [0,0,0,0]

    # 向汇总的列表total_total_dict中，填充已有的数量
    for key,value in total_dict.items():  # 遍历total_dict中的每种分组：20、50、100、1000
        site_num = class_list.index(int(key))  # 当前分组所在的位置

        # print('site_num' , key , site_num)
        for _i in value:  # 遍历分组中的所有操作记录
            total_total_dict[_i][site_num] = value[_i]  # 赋值

    # print('total_dict:\n%s\n' % total_dict)
    # print('txt_dict:\n%s\n' % txt_dict)
    # print('total_total_dict:\n%s\n' % total_total_dict)

    # 生成数据报告文件
    with open('res/action/statistics_report.txt','w',encoding='utf-8') as save_file:

        # 添加表头
        save_file.write('类型/数量')
        for i in class_list:
            save_file.write('\t%s次' % i)
        save_file.write('\r\n')

        # 显示数量
        for key,value in total_total_dict.items():
            save_file.write(key)

            for i_value in value:
                # print(i_value)
                save_file.write('\t')
                save_file.write(str(i_value))

            save_file.write('\r\n')

        save_file.write('\r\n\r\n\r\n############################################\r\n\r\n\r\n')

        # 添加表头
        save_file.write('类型/几率')
        for i in class_list:
            save_file.write('\t%s次' % i)
        save_file.write('\r\n')

        # 按比例显示
        for key,value in total_total_dict.items():
            save_file.write(key)

            a = 0  # 用来标记怎么取值
            for i_value in value:
                if i_value == 0:
                    save_file.write('\t')
                    save_file.write('0')
                    a += 1
                else:
                    r_key = class_list[a]
                    _total = txt_dict[str(r_key)]['总操作次数']  # 总数
                    # print(i_value)
                    save_file.write('\t')
                    save_file.write('%.2f%%' % (i_value / _total * 100))
                    a += 1

            save_file.write('\r\n')

    # 生成迷你报告文件
    with open('res/action/mini_report.txt','w',encoding='utf-8') as save_file:
        for key,value in txt_dict.items():
            save_file.write('操作在%s以下的用户操作数据:' % key)
            for i,j in value.items():
                save_file.write('\r\n%s:%0.1f' % (i,j))
            save_file.write('\r\n\r\n\r\n############################################\r\n\r\n\r\n')


# 不区分日期，统计ID的行为频率
def outside_date():
    file_path = 'res/action'

    if not os.path.exists(file_path):  # 如果没有文件，则结束
        print('找不到文件夹：%s\n' % file_path)
        exit()

    file_list = os.listdir(path)  # 获取文件夹的所有文件和目录
    # print(file_list)

    # 扫描文件夹，将内容中的操作按照时间的方式分类计数，生成列表
    action_list = [{} for i in range(31)]  # 创建一个包含31个字典的list，每天list中是包含各种行为数量的字典
    for i in file_list:  # 遍历文件列表
        if i[0] == '.':
            continue
        with open('%s/%s' % (file_path,i),'r',encoding='UTF-8') as _file:
            _list = _file.readlines()

            for i_list in _list:
                _action = i_list.replace('\n','').split("\t")[1]  # 获取动作
                _day = int(i_list.split(" ")[0].split("-")[2])  # 获取日期
                # print(i_list.split(" "))

                if _action in action_list[_day - 1]:
                    action_list[_day - 1][_action] += 1
                else:
                    action_list[_day - 1][_action] = 1
        # break
    print('扫描文件完成：%s' % len(action_list))

    # 将所有的操作汇集在一个表中
    total = {}
    for i in action_list:
        if i:  # 如果不为空
            for key,value in i.items():
                if key in total:
                    total[key] += value
                else:
                    total[key] = value

    # print(total)

    # 将汇总内容保存下来
    with open('res/dee.txt','w') as file:
        for key,value in total.items():
            file.write('%s\t%s\r' % (key,value))

    # 将每日操作计数，展示出来
    for i in action_list:
        if i:  # 如果不为空
            key_list = []
            value_list = []
            for key,value in i.items():
                key_list.append(key)
                value_list.append(value)

            # make_pie(key_list,value_list)
        break

    #
    dfgd = dde(total,5)
    _dict = list(dfgd.items())  # 排序后的list
    _dict.sort(key=lambda x:x[1],reverse=True)  # 降序排序

    make_pie(_dict)  # shur


# 根据设备登录次数，生成用户报告
def report_for_days_by_device_id(tab):
    if not os.path.exists('%s/%s' % (path,'device_id')):  # 如果文件夹不存在，则新建
        print('文件夹不存在，生成中……')
        action_count().get_list_by_device_id()

    file_list = os.listdir('%s/%s' % (path,'device_id'))  # 获取文件夹的所有文件和目录
    # print(file_list)

    txt_dict = [[0,0,0,0,0],[0,0,0,0,0]]  # 概括报告,第一个为设备数，第二个为次数,[0,0]中,最后一个是总的报告数

    re_list = [{},{},{},{}]  # 生成列表：[{},{},{},{}] #统计用户操作次数
    # 遍历文件列表，根据当天的操作次数，统计每种操作的次数
    for i_file in file_list:
        if int(i_file.split('_')[0]) == 1:  # 提取登录天数，如果等于1 则继续

            txt_dict[0][-1] += 1  # 统计设备+1

            with open('res/user_action_report/device_id/%s' % i_file) as file:
                _list = file.readlines()

                # 遍历每一行内容,根据操作数，统计操作数
                for i in range(len(tab)):  # 遍历区间
                    if len(_list) < tab[i]:  # 如果满足当前的区间,则在对应的区间统计用户的操作次数

                        txt_dict[0][i] += 1  # 对应区间的设备数+1

                        for i_list in _list:
                            _key = i_list.split('\t')[1]  # 获得操作名
                            if _key in re_list[i]:
                                re_list[i][_key] += 1  # 对用区间的操作数 +1

                                txt_dict[1][i] += 1  # 对应区间的总操作 +1
                                txt_dict[1][-1] += 1  # 总设备数+1
                            else:
                                re_list[i][_key] = 1  # 对用区间的操作数 =1

                                txt_dict[1][i] += 1  # 对应区间的总操作 +1
                                txt_dict[1][-1] += 1  # 总操作数+1
                        break

    print('概括报告:%s' % txt_dict)

    # 遍历后，把内容放入数据报告
    total_dict = {}  # 数据报告,根据区间统计每个操作的数量
    for i in range(len(re_list)):  # 获取每个区间的数值

        for _i in re_list[i]:
            if _i in total_dict:  # 如果报告中有此相操作，则把值放到对应位置
                total_dict[_i][i] = re_list[i][_i]
            else:  # 如果报告中没有此类操作，则新建，并把值放到对应位置
                total_dict[_i] = [0,0,0,0]
                total_dict[_i][i] = re_list[i][_i]

    # 为了排序，所以要把字典变成列表，以后单独做
    print('数据报告:%s' % total_dict)

    ################################################################################################################################
    # 保存total_dict数据报告
    with open('%s/%s' % (path,'statistics_report.txt'),'w') as file:
        # 写入表头
        file.write('%s' % '操作类型')
        for i in tab:
            file.write('\t%s次' % i)
        file.write('\r')

        # 写入主体
        for key,value in total_dict.items():
            file.write('%s' % key.replace('\n',''))
            for i in range(len(value)):
                # print(value[i],txt_dict[i][1])
                file.write('\t%.2f%%' % (value[i] / txt_dict[1][i] * 100))  # 用百分比显示
            file.write('\r')
    print('生成数据报告')

    # 保存txt_dict概括报告
    with open('%s/%s' % (path,'mini_report.txt'),'w') as file:
        # 写入表头
        file.write('种类')
        for i in tab:
            file.write('\t%s次' % i)
        file.write('\r')

        # 写入设备数
        file.write('设备数')
        for i in txt_dict[0]:
            file.write('\t%s' % i)
        file.write('\r')

        # 写入操作数
        file.write('操作总数')
        for i in txt_dict[1]:
            file.write('\t%s' % i)
        file.write('\r')

        # 写入设备/操作数
        file.write('单设备操作数')
        for i in range(len(txt_dict)):
            file.write('\t%.2f' % (txt_dict[1][i] / txt_dict[0][i]))
        file.write('\r')
    print('生成数据报告')


def updata_file(list_file):
    """
    生成和更新目前的uid和device文件夹
    :param list_file: 要添加的文件名：'2018_09'
    :return:
    """
    for i in list_file:
        print('开始:%s' % i)
        a = get_txt(i)  # 生成txt文件

        print('开始:mak_uid_file')
        mak_uid_file(a)  # 更新到uid

        print('开始:make_device_file')
        make_device_file(a)  # 更新到uid


if __name__ == '__main__':
    """更新文件"""
    _list_file = ['2018_09','2018_10','2018_11','2018_12','2019_01','2019_02']  # 要添加的文件
    _special_file = ['clickHomeTopic']  # 添加特殊的文件
    r_file = _list_file[-1:]  # 要添加的文件
    # updata_file(r_file)#更新文件

    """按照一个条件，获取一个列表，并进行对用统计"""
    _list_visitor = _get_list_visitor()  # 获取游客列表
    _list_all_device = _get_list_all_device()  # 获取所有设备
    _list_few_day = _get_list_few_day()  # 获取登录N天设备

    """游客在进入帖子详情前，在哪个界面，显示最多多6个数据，生成饼状图"""
    d = show_view_time(_list_all_device).all_action  # 统计访问界面的次数
    make_pie(d[:6],'游客在看贴前的所处界面占比')  # 生成饼状图

    ## 提取只登录过一天的设备，并生成报告文件
    # a = _get_list_few_day() # 获取只登录一天的用户列表
    # b = show_view_time(a).last_action
    # make_pie(b[:6])

    # a = count_one_percent('首页-专题',_get_list_all_device())
    # show_home_times()

    # a = count_one_percent('首页-悬浮按钮',_get_list_all_device())
    # a = count_one_percent('帖子详情',_get_list_all_device())

    # find_device(216740)  # 找到登录过此用户的设备，确认一个用户用多少设备在使用，从而明确用户的粘性
    # _example = ['001_0A1E920F-ECF5-4A2D-A58D-DC20BAD39596','001_0DDB58A4-A050-46FA-BA08-230E2E33AE8C']
    #
    # see_device(_example)  # 查看单个设备的情况
    #
    # count_one_percent('首页',_example)

    # device_last()
    # # 输入区间，将只上线一天的设备统计并报告
    # TAB = [20,50,100,1000]
    # report_for_days_by_device_id(TAB)

    # create_report()  # 生成统计报告
    #
    # key = '社区首页'
    # trend_key(key)
    #
    # outside_date()  # 不区分日期，统计ID的行为频率

    # data=make_txt()  # 获取文件
    # mak_uid_file(data)  # 生成uid文件
