# coding=utf-8
"""
统计用户ID表的数据的工具
"""

# 公共库
import os  # 转换内容 ，并提取数据
import sys
from datetime import datetime

# 私有库
from tm51.tool import get_xml,new_folder,action_to_cn,make_pie,dde,make_bar

"""
# CREATE TABLE `user` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `username` varchar(64) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '用户名',
#   `password` varchar(128) NOT NULL DEFAULT '' COMMENT '密码',
#   `sex` tinyint(4) NOT NULL DEFAULT '2' COMMENT '性别 0保密 1男 2女',
#   `birth` date DEFAULT '1970-01-01' COMMENT '生日',
#   `geo_id` int(11) DEFAULT '0' COMMENT '地域',
#   `email` varchar(128) DEFAULT '' COMMENT '邮件',
#   `mobile` varchar(11) DEFAULT '' COMMENT '手机号',
#   `head_img` varchar(255) DEFAULT '' COMMENT '用户头像',
#   `salt` varchar(12) NOT NULL DEFAULT '' COMMENT '加密盐值',
#   `from_client` tinyint(4) DEFAULT '1' COMMENT '来源终端 1 pc 2 ios 3 android 4 wap',
#   `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '用户状态 默认 0 有效',
#   `is_virtual` tinyint(4) DEFAULT '0' COMMENT '0 真实用户； 1 虚拟用户',
#   `is_freeze` tinyint(4) DEFAULT '0' COMMENT '默认0 未冻结；1冻结（不能体现)',
#   `last_login_ip` varchar(64) DEFAULT '' COMMENT '最后登陆IP',
#   `last_login_time` timestamp NULL DEFAULT '0000-00-00 00:00:00' COMMENT '最后登陆日期',
#   `is_new` tinyint(4) DEFAULT '1' COMMENT '默认 0表示是不是新手 1是新手',
#   `is_pop` tinyint(4) DEFAULT '1' COMMENT '是否弹出过（设置状态时）默认1没弹出过；0已弹过',
#   `alipay_account` varchar(255) NOT NULL COMMENT '支付宝账号（姓名#支付宝账号）',
#   `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
#   `updated_at` timestamp NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `uni_username` (`username`),
#   KEY `idx_created_at` (`created_at`),
#   KEY `idx_mobile` (`mobile`),
#   KEY `idx_virtual` (`is_virtual`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';
"""

tops_num = 8  # 设置显示前几名的内容
_split_ = '\t'  # 统计报告的分隔符号
name = 'user'
path = new_folder('res/%s' % name)
path_date_file = new_folder('%s/date' % path)

list_key = ['id','username','sex','birth','geo_id','email','mobile','head_img','from_client','is_virtual',
            'last_login_ip','is_new','is_pop','alipay_account','created_at','updated_at']  # 简版字段
site_id = list_key.index('id')  # id位置
site_username = list_key.index('username')  # username位置
site_sex = list_key.index('sex')  # sex位置
site_birth = list_key.index('birth')  # birth位置
site_geo_id = list_key.index('geo_id')  # geo_id位置
site_email = list_key.index('email')  # email位置
site_mobile = list_key.index('mobile')  # mobile位置
site_head_img = list_key.index('head_img')  # head_img位置
site_from_client = list_key.index('from_client')  # from_client位置
site_is_virtual = list_key.index('is_virtual')  # is_virtual位置
site_last_login_ip = list_key.index('last_login_ip')  # last_login_ip位置
site_is_new = list_key.index('is_new')  # is_new位置
site_is_pop = list_key.index('is_pop')  # is_pop位置
site_alipay_account = list_key.index('alipay_account')  # alipay_account位置
site_created_at = list_key.index('created_at')  # created_at位置
site_updated_at = list_key.index('updated_at')  # updated_at位置

"""生成文件"""


def get_txt():
    """
    传入name_date为:2019_02
    从user_action_report文件夹中的txt文件夹中查找对应文件
    如果没有txt文件，则从xml文件夹中查找对应xml文件，生成txt文件。则返回此文件的内容
    如果有文件，则返回此文件的内容
    :return: 返回整个数据表，单个元素参考list_key
    """
    print('开始：%s' % sys._getframe().f_code.co_name)
    path_txt = r'%s/txt/%s.txt' % (path,name)
    # print(path_txt)
    if os.path.exists(path_txt):  # 如果有文件，则读取文件，并返回
        with open(path_txt,'r') as file:
            _file = eval(file.read())

        print(r'找到文件：%s' % path_txt)
        # print(r'找到文件：%s' % _file)
        return _file  # 转换数据，获取想要的字段
    else:  # 如果没有文件，则读取xml，保存txt，并返回
        _file = get_xml(name,list_key)

        with open(path_txt,'w') as file:  # 保存内容
            file.write(str(_file))

        print(r'找到文件：%s' % path_txt)
        # print(r'找到文件：%s' % _file)
        return _file  # 转换数据，获取想要的字段


def make_date_file(data):
    """
    根据txt文件，按照用户的注册月份，同一个月份的用户放在一个文件夹中
    ('1', 'admin', '2', '1990-01-01', '1156420100', 'admin@tm51.com', '', 'avatar/000/00/00/01_avatar_big.jpg', '1', '0', '171.43.187.251', '0', '0', '', '2004-01-16 12:23:50', '2019-01-22 18:15:45')
    :return:
    """
    print('开始：%s' % sys._getframe().f_code.co_name)

    data.sort(key=lambda x:x[site_created_at])  # 按照注册日期升序

    _list = dict()  # 返回值，按照年月分类数据

    _v = 0  # 序号

    _plan = 0  # 进度统计
    for _one_data in data:
        if _one_data[site_is_virtual] == '0':  # 屏蔽虚拟用户
            _date = _one_data[site_created_at][:7]  # 获取创建时间
            # print(_date)

            _list[_date] = _list.get(_date,[]) + [_one_data]  # 添加此条信息

            _plan += 1
            print(r'更新进度 (%s/%s)' % (_plan,len(data)))

    # print(_list)
    for key,value in _list.items():  # 保存数据
        print(key,value)
        with open('%s/%s_%s' % (path_date_file,key,len(value)),'w') as file:
            file.write(str(value))

    return _list


"""统计"""


def _get_vip_yaer(_year):
    """
    获取对应年份的注册用户数据，并制作柱状图
    :param _year:
    :return:
    """
    print('开始：%s' % sys._getframe().f_code.co_name)

    list_file = dict()
    for i in os.listdir(path_date_file):
        _y = i.split('-')[0]
        if _y == _year:  #
            _i = i.split('_')
            list_file[_i[0].split('-')[1]] = _i[1]

    make_bar(list_file,'%s年每月注册用户数' % _year)

def updata_file():
    """
    生成和更新目前的txt文件夹
    :return:
    """
    print('开始：%s' % sys._getframe().f_code.co_name)

    data = get_txt()
    make_date_file(data)


if __name__ == '__main__':
    # updata_file()  # 生成文件

    _get_vip_yaer('2018')#获取指定年份的注册注册用户数据


    # data=make_txt()  # 获取文件
    # make_file(data)  # 生成月份文件
    # make_chart()  # 生成注册用户表格
